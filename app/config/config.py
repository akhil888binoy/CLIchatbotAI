import os 
from dotenv import load_dotenv

load_dotenv()

ollama_api = os.getenv('OLLAMA_API')