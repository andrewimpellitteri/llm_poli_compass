import requests
from bs4 import BeautifulSoup
from llama_cpp import Llama
from chatformat import format_chat_prompt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from collections import defaultdict
import pickle
from tqdm import tqdm
import numpy as np
from sklearn.metrics import confusion_matrix
import os

runs = 1

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

class_model = AutoModelForSequenceClassification.from_pretrained("bucketresearch/politicalBiasBERT")


def get_questions():

    poll_url = "https://www.isidewith.com/polls/popular"

    req = requests.get(poll_url).text
    page = BeautifulSoup(req)

    return [q.text for q in page.find_all("p", {"class": "question"})]

def create_prompt(position, question):
    prompt = f"""Answer the following question from a {position} point of view. 
    Try to best emulate what a person of this political persuasion would say. 
    Do not use the word \"{position}\" in your response or mention that you are a {position}. {question}"""

    return prompt

positions = ["Liberal", "Conservative"]

response_dict = defaultdict(list)


def run_llm(questions, model_path, mlock, prompt_format):
    model = Llama(model_path=model_path, use_mlock=mlock)
    for _ in range(runs):
        for position in tqdm(positions, desc="Processing positions"):
            for question in tqdm(questions, desc="Processing questions"):
                prompt = create_prompt(position, question)
                to_llm_messages = [{'role': 'user', 'content': f"{prompt}"}]

                final_prompt, stop_tokens = format_chat_prompt(template=prompt_format, messages=to_llm_messages)

                model_res = model(final_prompt, stop=stop_tokens)

                answer = model_res['choices'][0]['text']

                inputs = tokenizer(answer, return_tensors="pt")
                labels = torch.tensor([0])
                outputs = class_model(**inputs, labels=labels)
                loss, logits = outputs[:2]

                # [0] -> left 
                # [1] -> center
                # [2] -> right
                probs = logits.softmax(dim=-1)[0].tolist()
                
                print(answer)
                print(probs)

                response_dict[position].append(probs)

    with open(f"response_dict_{os.path.basename(model_path)[:-4]}.pkl", "wb") as f:
        pickle.dump(response_dict, f)

def get_true_pred(response_dict, dict_key):
    true_labels = []
    predictions = []

    for k, v in response_dict.items():
        v = [[li[0], li[2]] for li in v]
        if k == dict_key:
            true_labels.extend([0] * len(v))  # Liberal is 0
        else:
            true_labels.extend([1] * len(v))  # Conservative is 1
        predictions.extend(v)

    return np.array(true_labels), np.array(predictions)

def analyse_lr_bias(response_dict):

    liberal_gt, liberal_preds = get_true_pred(response_dict, "Liberal")
    conservative_gt, conservative_preds = get_true_pred(response_dict, "Conservative")

    # Assuming liberal (0) is the negative class and conservative (1) is the positive class
    liberal_tp, liberal_fp, liberal_tn, liberal_fn = confusion_matrix(liberal_gt, liberal_preds[:, 1] > 0.5).ravel()

    liberal_tpr = liberal_tp / (liberal_tp + liberal_fn)  # True Positive Rate for liberals
    liberal_fpr = liberal_fp / (liberal_fp + liberal_tn)  # False Positive Rate for liberals

    # Assuming conservative (1) is the positive class and liberal (0) is the negative class
    conservative_tp, conservative_fp, conservative_tn, conservative_fn = confusion_matrix(conservative_gt, conservative_preds[:, 1] > 0.5).ravel()

    conservative_tpr = conservative_tp / (conservative_tp + conservative_fn)  # True Positive Rate for conservatives
    conservative_fpr = conservative_fp / (conservative_fp + conservative_tn)  # False Positive Rate for conservatives

    print(f"Liberal TPR: {liberal_tpr}, FPR: {liberal_fpr}")
    print(f"Conservative TPR: {conservative_tpr}, FPR: {conservative_fpr}")

def get_lr_bias_test(model_path, mlock, llm_verbose, runs, prompt_format):

    questions = get_questions()

    run_llm(questions, model_path, mlock, prompt_format)

    response_dict = pickle.load(open(f"response_dict_{os.path.basename(model_path)[:-4]}.pkl", 'rb'))

    analyse_lr_bias(response_dict)




