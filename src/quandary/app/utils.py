
from llama_index import VectorStoreIndex, download_loader, StorageContext, load_index_from_storage
from llama_index.node_parser import SimpleNodeParser
from dotenv import load_dotenv
import openai
import os

def run_quandary(question):

    # Run
    load_dotenv()

    # Constants
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    QNDY_DOCS_PATH = os.environ['QNDY_DOCS_PATH']
    QNDY_INDEX_PATH = os.environ['QNDY_INDEX_PATH']
    openai.api_key = OPENAI_API_KEY

    reader = download_loader('ObsidianReader')
    documents = reader(QNDY_DOCS_PATH).load_data()
   
    # parse nodes from documents
    parser = SimpleNodeParser()
    nodes = parser.get_nodes_from_documents(documents)

    if os.path.exists(QNDY_INDEX_PATH):
        # index already exists, so load it in
        storage_context = StorageContext.from_defaults(persist_dir=QNDY_INDEX_PATH)
        index = load_index_from_storage(storage_context)
    else:
        # create index and persist it
        index = VectorStoreIndex(nodes)
        index.storage_context.persist()

    query_engine = index.as_query_engine()

    response = query_engine.query(question)
    return response