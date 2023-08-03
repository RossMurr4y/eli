# ChatBot for Local Markdown

botbot - a local chatbot for your personal documents.

> botbot: get to the bottom of things!

## Setup

```bash
brew install python

pip3 install --upgrade build

python3 -m build

# install locally, under the alias 'umm'
pip3 install --editable . 
```

Check its all setup with `umm --help`

## First Time Usage

1. Replace {KEY} with your OPENAI API Key, and run `echo 'OPENAI_API_KEY={KEY}' > .env`
1. Replace {PATH} with your local filepath to the obsidian vault, then run `echo 'BOTBOT_DOCS_PATH={PATH}' >> .env`
1. Replace {PATH} with a directory you would like to store your local index files, then run `echo 'BOTBOT_INDEX_PATH={PATH}' >> .env`

Your final .env file should look like this:

```ini
OPENAI_API_KEY=sk-123123123123123123123123123123123123123123
BOTBOT_DOCS_PATH=/Users/yourname/Documents/exampledir
BOTBOT_INDEX_PATH=./exampledir
```

Then follow the usage section below.

## Usage

Botbot installs under the alias `umm` as in __umm what's the airspeed of an unladen swallow?__.

Basic usage is `umm "{question}"`.

> don't forget the quotes!

For full syntax, run `umm --help`