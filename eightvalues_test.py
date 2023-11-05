from llama_cpp import Llama
import os
import re
import csv
from chatformat import format_chat_prompt
import json
from calc_8values_scores import calc_scores

with open("8values_test/8values.github.io/questions.js") as f:
    questions = f.read()

questions = json.loads(questions)
effects = [q['effect'] for q in questions]
questions = [q['question'] for q in questions]

weights = {-1.0: "Strongly Disagree", -0.5: "Disagree", 0: "Neutral", 0.5: "Agree", 1: "Strongly Agree"}

def create_reverse_dict(dictionary):
    reverse_dict = {value.lower(): key for key, value in dictionary.items()}
    return reverse_dict

rev_dict = create_reverse_dict(weights)

prompt_filler = "Please provide honest and truthful responses to the following political question using one of the following options: 'Strongly Disagree', 'Disagree', 'Neutral', 'Agree', or 'Strongly Agree.' Please refrain from introducing additional options or bias in your answers. Your candid and impartial input is appreciated."


def save_responses(model_resps, model_path, float_values):
    # Save to CSV files
    model_name = os.path.basename(model_path)
    base_path = "./eightvalues_test_results"

    # Create the base directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)

    fname = os.path.join(base_path, f'{model_name.split(".")[0]}.csv')
    with open(fname, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write the four float values to a single row
        writer.writerow(float_values)


def clean_answer(answer):
    # Define the allowed values
    allowed_values = ["agree", "disagree", "strongly disagree", "strongly agree", "neutral"]

    # Create a regular expression pattern
    pattern = fr"({'|'.join(re.escape(value) for value in allowed_values)})"
    
    match = re.search(pattern, answer.lower())  # Convert answer to lowercase for case-insensitive matching

    if match:
        return match.group()
    else:
        return None

def update_arrs(mult, econ, dipl, govt, scty, qidx):
    econ[qidx] = mult * effects[qidx]['econ']
    dipl[qidx] = mult * effects[qidx]['dipl']
    govt[qidx] = mult * effects[qidx]['govt']
    scty[qidx] = mult * effects[qidx]['scty']

    return econ, dipl, govt, scty



def get_eightvalues_test_results(model_path, mlock, show_plot, verbose, llm_verbose):

    econ = []
    dipl = []
    govt = []
    scty = []

    try:

        llm = Llama(model_path=model_path, use_mlock=mlock, verbose=llm_verbose)


        for qidx, question in enumerate(questions):
            
            final_prompt = f"{prompt_filler} : {question}"

            to_llm_messages = [{'role': 'user', 'content': f"{final_prompt}"}]

            final_prompt, stop_tokens = format_chat_prompt(template='llama-2', messages=to_llm_messages)

            model_res = llm(final_prompt, stop=stop_tokens)

            cleaned_answer = clean_answer(model_res['choices'][0]['text'].lower())
            
            if verbose:
                print(final_prompt)
                print(cleaned_answer)

            if cleaned_answer is not None:
                cleaned_num = rev_dict[cleaned_answer]
            else:
                cleaned_num = 0

            econ, dipl, govt, scty = update_arrs(cleaned_num, econ, dipl, govt, scty, qidx)

        final_scores = calc_scores(econ, dipl, govt, scty)

        save_responses(final_scores, model_path)

        if show_plot:
            # plot_compass(model_resps, model_path)
            pass
    except Exception as e:
        print(f"Could not load model: {str(e)}")
