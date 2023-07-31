from llama_index import VectorStoreIndex, SimpleDirectoryReader, download_loader, StorageContext, load_index_from_storage
from dotenv import load_dotenv
import openai
import click
import os
import sys

@click.command()
@click.option('--question', help='Your question for botbot.')

def answer_question(question):
    """botbot: a local chatbot for your personal documents."""
    load_dotenv()

    parser = argparse.ArgumentParser(
        prog='Document Chat Bot',
        description='A chatbot for your documents')
    parser.add_argument('question')
    args = parser.parse_args()

    openai.api_key = os.environ['OPENAI_API_KEY']

    ObsidianReader = download_loader('ObsidianReader')
    documents = ObsidianReader('/Users/rossmurray/Documents/rei-obsidian-vault').load_data()

    if os.path.exists('./storage'):
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        index = load_index_from_storage(storage_context)
    else:
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist()

    query_engine = index.as_query_engine()
    response = query_engine.query(args.question)
    print(response)

if __name__ == '__main__':
    answer_question()