import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv
import chromadb
from chromadb.utils.embedding_functions.openai_embedding_function import OpenAIEmbeddingFunction

OPENAI_API_KEY = "OPENAI_API_KEY"
RAG_NAME = "pixar_rag"
VECTOR_STORE_PATH = "./vector_store"

class RagAgent:
    """Class that contains the main logic of the RAG."""
    
    def __init__(self):
        # Load env
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv(OPENAI_API_KEY))
        # Set ChromaDB with OpenAI embeddings
        self.chroma_client = chromadb.PersistentClient(path=VECTOR_STORE_PATH)
        self.embedding_function = OpenAIEmbeddingFunction(api_key=self.client.api_key)
        self.collection = self.chroma_client.get_or_create_collection(
            name=RAG_NAME, 
            embedding_function=self.embedding_function,
            )
        
    def load_and_store_csv(self, file_path:str) -> None:
        """Load and store the csv into the vector_store

        Args:
            file_path (str): CSV path
        """
        df = pd.read_csv(file_path)
        
        for ind, row in df.iterrows():
            doc_text = ", ".join([f"{col}: {str(row[col])}" for col in df.columns])
            self.collection.add(ids=[str(ind)], documents=[doc_text])
        
        print("CSV indexed in vector_store.\n")
        
    def retrieve_relevant_data(self, query:str) :
        """Retrieve the relevant data based on the vector_store

        Args:
            query (str): Query text
        """
        results = self.collection.query(query_texts=[query], n_results=3)
        return results["documents"][0] if results["documents"] else []