from dotenv import load_dotenv
from .mode import ModeInterface
from .response import ResponseInterface

from llama_index import (
    VectorStoreIndex,
    download_loader,
    StorageContext,
    load_index_from_storage,
    Response,
)
from llama_index.schema import MetadataMode
from llama_index.node_parser import SimpleNodeParser
from dotenv import load_dotenv
import openai
import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


class ResponseLangChain(ResponseInterface):
    """A response from the LangChain LLM"""

    value = ""


class ResponseLlamaIndex(ResponseInterface):
    """A response from Llama via Llama Index"""

    value = ""


class ModeLlamaIndex(ModeInterface):
    """A mode that uses Llama Index"""

    question = ""
    response = ResponseLlamaIndex()

    def __init__(self):
        # Run
        load_dotenv()

    def run(self) -> ResponseLlamaIndex:
        # Constants
        OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
        QNDY_DOCS_PATH = os.environ["QNDY_DOCS_PATH"]
        QNDY_INDEX_PATH = os.environ["QNDY_INDEX_PATH"]
        QNDY_DEBUG = os.environ.get("QNDY_DEBUG", "False") in [
            "True",
            "1",
            "true",
        ]
        openai.api_key = OPENAI_API_KEY

        reader = download_loader("ObsidianReader")
        documents = reader(QNDY_DOCS_PATH).load_data()

        # parse nodes from documents
        parser = SimpleNodeParser()
        nodes = parser.get_nodes_from_documents(documents)

        if os.path.exists(QNDY_INDEX_PATH):
            # index already exists, so load it in
            storage_context = StorageContext.from_defaults(
                persist_dir=QNDY_INDEX_PATH
            )
            index = load_index_from_storage(storage_context)
        else:
            # create index and persist it
            index = VectorStoreIndex(nodes)
            index.storage_context.persist()

        query_engine = index.as_query_engine()

        if QNDY_DEBUG:
            debug_output = f"""
            ```
            Debug: Enabled
            Documents: {len(documents)}
            Nodes: {len(nodes)}
            ```
            """
            original_response = query_engine.query(self.question)
            response = ResponseLlamaIndex()
            response.value = Response(
                response=original_response.response + "\n\n" + debug_output,
                source_nodes=original_response.source_nodes,
                metadata=original_response.metadata,
            )
        else:
            response = ResponseLlamaIndex()
            response.value = query_engine.query(self.question)
        return response


class ModeLangChain(ModeInterface):
    """A mode that uses LangChain LLM"""

    question = ""
    response = ResponseLangChain()

    def __init__(self):
        load_dotenv()
        # Constants
        OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
        # QNDY_DOCS_PATH = os.environ["QNDY_DOCS_PATH"]
        # QNDY_INDEX_PATH = os.environ["QNDY_INDEX_PATH"]
        # QNDY_DEBUG = os.environ.get("QNDY_DEBUG", "False") in ["True", "1", "true"]
        openai.api_key = OPENAI_API_KEY

    def run(self) -> ResponseLangChain:
        chat_model = ChatOpenAI()
        messages = [HumanMessage(content=self.question)]
        prediction = chat_model.predict_messages(messages)
        response = ResponseLangChain()
        response.value = prediction.content
        return response
