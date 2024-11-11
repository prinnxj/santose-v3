from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

class RAGEngine:
    def __init__(self, embeddings):
        # Load environment variables
        load_dotenv()
        
        # Initialize the language model
        self.llm = ChatOpenAI(
            model_name="gpt-4-turbo-preview",
            temperature=0,
            openai_api_key=os.getenv('OPENAI_API_KEY')
        )
        
        self.embeddings = embeddings
        self.vector_store = None
        self.qa_chain = None

    def create_vector_store(self, documents):
        # Create vector store from documents
        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings
        )
        
        # Create QA chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever()
        )

    def ask(self, question):
        if not self.qa_chain:
            return "Please load documents first."
        
        return self.qa_chain.run(question)