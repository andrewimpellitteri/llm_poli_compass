from classic_test import get_classic_test_results
from collections import defaultdict
import os
import pickle
from plot_all import plot_character_results
from tqdm import tqdm

character_prompts = {
    "Lib-Left": "an individual who advocates for both individual liberties and economically leans towards left-wing ideologies. They prioritize personal freedom, voluntary cooperation, and advocate for social equality and justice through collective action.",
    
    "Lib-Right": "someone who strongly supports individual liberties and leans towards right-wing economic ideologies. They emphasize personal responsibility, free-market principles, and champion minimal government intervention in both social and economic spheres. ",
    
    "Auth-Left": "an individual who favors strong central authority and aligns with left-wing economic ideologies. They advocate for collective ownership and control of resources, prioritize social equality, and often support governmental intervention to address societal disparities.",
    
    "Auth-Right": "someone who supports a strong central authority and leans towards right-wing economic beliefs. They emphasize traditional values, law and order, and prioritize national sovereignty and security."
}

def save_char_responses(model_path, character_resps):
    # Saving the character_resps dictionary to a file
    dir_name = "./character_test_results"
    os.makedirs(dir_name, exist_ok=True)  # Create the directory if it doesn't exist

    file_name = os.path.basename(model_path) + ".pickle"
    file_path = os.path.join(dir_name, file_name)

    with open(file_path, 'wb') as file:
        pickle.dump(character_resps, file)


def get_character_test_results(model_path, mlock, show_plot, verbose, llm_verbose, runs, prompt_format, plot_file):

    if plot_file is not None:
        plot_character_results(model_path, [], load_from_file=plot_file)
    
    orig_prompt_filler = "You must use exactly one of the following options: 'Strongly Disagree', 'Disagree', 'Agree', or 'Strongly Agree.' Please refrain from introducing additional options in your answers. The question is: "

    character_resps = defaultdict(list)

    for character in tqdm(character_prompts.keys(), desc="character"):
        
        character_prompt = f"Answer the following political question acting as a person who is {character_prompts[character]}"
        
        prompt = character_prompt + orig_prompt_filler

        model_resps = get_classic_test_results(
            model_path, mlock, 
            show_plot, 
            verbose, 
            llm_verbose,
            runs, 
            prompt, 
            prompt_format, 
            True)

        character_resps[character] = model_resps

    # save character_resps

    save_char_responses(model_path, character_resps)

    # plot results

    plot_character_results(model_path, character_resps)