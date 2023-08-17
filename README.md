# Quandary

Local Q-and-A with your personal documents.

## Setup

```bash
brew install python

pip3 install --upgrade build

python3 -m build

# install locally, under the alias 'quandary'
pip3 install --editable . 
```

Check its all setup with `quandary`

## First Time Usage

1. Replace {KEY} with your OPENAI API Key, and run `echo 'OPENAI_API_KEY={KEY}' > .env`
1. Replace {PATH} with your local filepath to the obsidian vault, then run `echo 'QNDY_DOCS_PATH={PATH}' >> .env`
1. Replace {PATH} with a directory you would like to store your local index files, then run `echo 'QNDY_INDEX_PATH={PATH}' >> .env`

Your final .env file should look like this:

```ini
OPENAI_API_KEY=sk-123123123123123123123123123123123123123123
QNDY_DOCS_PATH=/Users/yourname/Documents/exampledir
QNDY_INDEX_PATH=./exampledir
```

Then follow the usage section below.

## Usage

Quandary installs as a command-line tool. After installation, you can launch it from any terminal by typing `quandary` followed by the `Enter` key.

## Development

```bash
# install the textual cli for development mode
pip3 install --upgrade textual-dev

# run quandary in "live-edit" mode
textual run --dev src/quandary/__init__.py
```