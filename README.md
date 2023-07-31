# ChatBot for Local Markdown

## Setup

1. `brew install python`
1. `python3 -m venv my_env`
1. `source my_env/bin/activate`
1. `pip3 install -r requirements.txt`
1. Replace {KEY} with your OPENAI API Key, and run `echo 'OPENAI_API_KEY={KEY}' > .env`
1. Replace {PATH} with your local filepath to the obsidian vault, then run `echo 'OBSIDIAN_VAULT_PATH={PATH}' >> .env`

## Usage

From the root of this repo:

1. [once per session] activate the python environment `source my_env/bin/activate`

Then to ask a question:

1. `python3 run.py "{question}"`
