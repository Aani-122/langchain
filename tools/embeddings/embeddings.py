from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")