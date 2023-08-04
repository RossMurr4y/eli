from llama_index import VectorStoreIndex, SimpleDirectoryReader, download_loader, StorageContext, load_index_from_storage
from dotenv import load_dotenv
import openai
import os
import argparse

def run_botbot(question):

    # Run
    load_dotenv()

    # Constants
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    BOTBOT_DOCS_PATH = os.environ['BOTBOT_DOCS_PATH']
    BOTBOT_INDEX_PATH = os.environ['BOTBOT_INDEX_PATH']
    openai.api_key = OPENAI_API_KEY

    reader = download_loader('ObsidianReader')
    documents = reader(BOTBOT_DOCS_PATH).load_data()

    if os.path.exists(BOTBOT_INDEX_PATH):
        # index already exists, so load it in
        storage_context = StorageContext.from_defaults(persist_dir=BOTBOT_INDEX_PATH)
        index = load_index_from_storage(storage_context)
    else:
        # create index and persist it
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist()

    query_engine = index.as_query_engine()

    response = query_engine.query(question)
    return response