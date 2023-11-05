""""Usage:
test_llm [MODEL_PATH] [TEST_TYPE] [PROMPT_FORMAT] [options]

Options:
--use_mlock
--show_plot

"""

from classic_test import get_classic_test_results
from eightvalues_test import get_8values_test_results
from docopt import docopt

run_classic_test = True

if __name__ == '__main__':

    arguments = docopt(__doc__)

    model_path = arguments['MODEL_PATH']
    test_type = arguments['TEST_TYPE']
    mlock = arguments['--use_mlock']

    prompt_format = arguments["PROMPT_FORMAT"]
    show_plot = arguments["--show_plot"]

    if test_type.lower() == 'classic':
        get_classic_test_results(model_path, mlock, show_plot)
    else:
        get_8values_test_results(model_path, mlock, show_plot)
    