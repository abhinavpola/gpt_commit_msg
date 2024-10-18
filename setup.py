from setuptools import setup, find_packages

setup(
    name="llm_commit_hook",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "litellm",
    ],
    entry_points={
        "console_scripts": [
            "install-commit-hook=llm_commit_hook.install_hook:install_hook",
        ],
    },
)
