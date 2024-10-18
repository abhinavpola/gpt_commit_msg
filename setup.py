from setuptools import setup, find_packages

setup(
    name="commit_msg_hook",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "litellm",
    ],
    entry_points={
        "console_scripts": [
            "install-commit-hook=commit_msg_hook.install_hook:install_hook",
        ],
    },
)
