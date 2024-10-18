import os
import shutil


def install_hook():
    # Get the path to the current repository's .git/hooks directory
    repo_path = os.getcwd()
    git_hooks_dir = os.path.join(repo_path, ".git", "hooks")

    if not os.path.exists(git_hooks_dir):
        raise Exception("This does not appear to be a Git repository.")

    # Path to the prepare-commit-msg hook template
    hook_template = os.path.join(
        os.path.dirname(__file__), "templates", "prepare-commit-msg"
    )

    # Destination where the hook will be copied
    destination = os.path.join(git_hooks_dir, "prepare-commit-msg")

    # Copy the hook template to the .git/hooks directory
    shutil.copyfile(hook_template, destination)

    # Make the hook script executable
    os.chmod(destination, 0o755)

    print("Git hook installed successfully.")


if __name__ == "__main__":
    install_hook()
