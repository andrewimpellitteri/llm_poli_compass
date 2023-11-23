""""Usage:
test_llm [MODEL_PATH] [TEST_TYPE] [PROMPT_FORMAT] [options]

Options:
--use_mlock
--no-show_plot
--verbose
--llm_verbose
-r runs
-p prompt
--plot_all_classic
--plot_all_eightvalues
"""

from classic_test import get_classic_test_results
from eightvalues_test import get_eightvalues_test_results
from docopt import docopt
from plot_all import plot_all_classic, plot_all_eightvalues
from left_right_bias import get_lr_bias_test
from character_test import get_character_test_results

run_classic_test = True

if __name__ == '__main__':

    arguments = docopt(__doc__)

    model_path = arguments['MODEL_PATH']
    test_type = arguments['TEST_TYPE']
    mlock = arguments['--use_mlock']

    prompt_format = arguments["PROMPT_FORMAT"]
    show_plot = not arguments.get('--no-show_plot', False)  # Set show_plot to True by default

    plot_all_classic_arg = arguments.get('--plot_all_classic')
    plot_all_eightvalues_arg = arguments.get('--plot_all_eightvalues')
    
    runs = int(arguments['-r'] or 1)
    print(f"runs: {runs}")
    verbose = arguments["--verbose"]
    llm_verbose = arguments["--llm_verbose"]

    # Check if the "--prompt" key exists
    if "-p" in arguments:
        prompt = arguments["-p"]
    else:
        prompt = None

    if test_type.lower() == 'classic':
        ret = get_classic_test_results(model_path, mlock, show_plot, verbose, llm_verbose, runs, prompt, prompt_format, character_mode=False)

    if test_type.lower() == 'lr_bias':
        get_lr_bias_test(model_path, mlock, llm_verbose, runs, prompt_format)

    if test_type.lower() == 'character':
        get_character_test_results(model_path, mlock, show_plot, verbose, llm_verbose, runs, prompt_format)
    else:
        get_eightvalues_test_results(model_path, mlock, show_plot, verbose, llm_verbose, runs, prompt, prompt_format)

    if plot_all_classic_arg:
        plot_all_classic()

    if plot_all_eightvalues_arg:
        plot_all_eightvalues()

    