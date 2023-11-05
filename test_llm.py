""""Usage:
test_llm [MODEL_PATH] [TEST_TYPE] [PROMPT_FORMAT] [options]

Options:
--use_mlock
--no-show_plot
--verbose
--llm_verbose

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
    
    verbose = arguments["--verbose"]
    llm_verbose = arguments["--llm_verbose"]

    if test_type.lower() == 'classic':
        get_classic_test_results(model_path, mlock, show_plot, verbose, llm_verbose)
    else:
        get_eightvalues_test_results(model_path, mlock, show_plot, verbose, llm_verbose)
    