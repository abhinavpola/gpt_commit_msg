import configparser
import subprocess
import litellm
import sys


def get_git_diffs():
    # Get the diffs using Git command
    diffs = subprocess.check_output(
        ["git", "diff", "--cached"], universal_newlines=True
    )
    return diffs


def load_llm_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    api_key = config.get("llm", "api_key")
    model = config.get("llm", "model")
    return api_key, model


def generate_commit_message(diffs, api_key, model):
    # Set the API key and model for litellm
    litellm.api_key = api_key
    response = litellm.completion(model=model, prompt=diffs, max_tokens=100)

    # Return the generated message
    return response["choices"][0]["text"].strip()


if __name__ == "__main__":
    # Get diffs
    diffs = get_git_diffs()

    # Load API key and model from config
    api_key, model = load_llm_config(".llmconfig")

    # Generate commit message
    commit_message = generate_commit_message(diffs, api_key, model)

    # Print the commit message to be captured in the Git hook
    print(commit_message)
