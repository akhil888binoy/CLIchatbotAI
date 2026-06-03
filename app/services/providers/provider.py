
from ollama_provider import send_ollama

from models import Conversation

def send_message( message: Conversation , provider: str):

    if provider == 'OLLAMA':
        response = send_ollama(message)
        return response
    else :
        print("Give valid provider")
    

