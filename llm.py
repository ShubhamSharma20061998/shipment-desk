# llm.py
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables once when this module is imported
load_dotenv()

# Initialize and export the reusable LLM instance
llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)