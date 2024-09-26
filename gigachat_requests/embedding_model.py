from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
)
from chromadb.config import Settings
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import GigaChatEmbeddings


class EmbeddingModel:
    def __init__(self, api_key):
        self.api_key = api_key
        self.documents = self.cut_the_document()
        self.db = self.create_embedding_model()

    def cut_the_document(self):
        loader = TextLoader('data/test.txt')
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=75)
        documents = text_splitter.split_documents(documents)
        print(documents)
        return documents

    def create_embedding_model(self):
        embeddings = GigaChatEmbeddings(
            credentials=self.api_key,
            verify_ssl_certs=False
        )
        database = Chroma.from_documents(
            self.documents,
            embeddings,
            client_settings=Settings(anonymized_telemetry=False),
            persist_directory='./'
        )
        return database
