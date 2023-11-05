""""Usage:
test_llm [MODEL_PATH] [TEST_TYPE] [options]

Options:
--use_mlock

"""

from classic_test import get_classic_test_results
from docopt import docopt

run_classic_test = True

if __name__ == '__main__':

    arguments = docopt(__doc__)

    model_path = arguments['MODEL_PATH']
    test_type = arguments['TEST_TYPE']
    mlock = arguments['--use_mlock']


    if test_type.lower() == 'classic':
        get_classic_test_results(model_path, mlock)
    else:
        pass
    