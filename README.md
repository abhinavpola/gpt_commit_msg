# Automatically generate commit messages

Just use `git commit -m` as usual, but you don't need to supply the commit message.

This git hook uses the LLM of your choice (model-switching powered by LiteLLM) and your commit diffs to generate the message.