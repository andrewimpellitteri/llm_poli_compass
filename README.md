# Political Compass Test LLM (Large Language Model) Utility

A utility for running tests on language models to evaluate their political bias. It supports both classic and eightvalues tests with various options. Uses the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) library for calling the llm.

## Usage

```
test_llm [MODEL_PATH] [TEST_TYPE] [PROMPT_FORMAT] [options]
```

### Options

- `--use_mlock`: Use mlock for memory management.
- `--no-show_plot`: Disable the display of plots (enabled by default).
- `--verbose`: Enable verbose mode.
- `--llm_verbose`: Enable verbose mode for the language model.

## Getting Started

1. Clone this repository to your local machine.

```
git clone https://github.com/your-username/test-llm-utility.git
```

2. Install the required dependencies using pip.

```
pip install -r requirements.txt
```

3. Run the utility by providing the necessary arguments.

```
python test_llm.py [MODEL_PATH] [TEST_TYPE] [PROMPT_FORMAT] [options]
```

## Example Usages

### Run a classic test on a language model:

```
python test_llm.py model_path/classic_model.pth classic "Prompt format" --use_mlock --verbose
```

### Run an eightvalues test on a language model:

```
python test_llm.py model_path/model.gguf eightvalues "Prompt format" --no-show_plot --llm_verbose
```

### Supported prompt formats

- Llama-2
- Alpaca
- Vicuna
- ChatLM

## License

This utility is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [docopt](https://github.com/docopt/docopt) for command-line argument parsing.
- 8values.github.io
- https://politicalcompass.github.io/
- [chatformat](https://github.com/Mwni/chatformat/tree/main)

