""""Usage:
test_llm [MODEL_PATH] [TEST_TYPE] [PROMPT_FORMAT] [options]

Options:
--use_mlock
--no-show_plot
--verbose
--llm_verbose
-r runs
-p prompt
"""

from classic_test import get_classic_test_results
from eightvalues_test import get_eightvalues_test_results
from docopt import docopt

run_classic_test = True

if __name__ == '__main__':

    arguments = docopt(__doc__)

    model_path = arguments['MODEL_PATH']
    test_type = arguments['TEST_TYPE']
    mlock = arguments['--use_mlock']

    prompt_format = arguments["PROMPT_FORMAT"]
    show_plot = not arguments.get('--no-show_plot', False)  # Set show_plot to True by default
    
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
        get_classic_test_results(model_path, mlock, show_plot, verbose, llm_verbose, runs, prompt)
    else:
        get_eightvalues_test_results(model_path, mlock, show_plot, verbose, llm_verbose, runs, prompt)
    