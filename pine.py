from tools.embeddings.embeddings import embeddings
import os 
from dotenv import load_dotenv
import pinecone
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
load_dotenv()

loader = TextLoader("C://Users//my_project//langchian_agent//sample3.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

index_name ='pdfchat'
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
vectorstore.add_documents(docs)

#docsearch = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)#name it as vector store 

'''
pc = Pinecone(
        api_key=os.environ.get("PINECONE_API_KEY")
    )
'''

#print(pc.list_indexes().names())
'''
vector_store=pc.form_existing_index(
    os.getenv("PINECONE_INDEX_NAME"),embeddings
)

vector_store.add_documents(docs)
'''