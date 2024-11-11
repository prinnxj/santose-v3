from langchain.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv

class EmbeddingManager:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize OpenAI embeddings
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            openai_api_key=os.getenv('OPENAI_API_KEY')
        )

    def get_embeddings(self):
        return self.embeddings