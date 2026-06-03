from storage.storage import load_current_conversation  , save_conversation
from providers.provider import send_message
from models.message import Message
from datetime import datetime


def chat_model(latest_msg: str , provider : str):
    
    conversation = load_current_conversation()
    latest_msg = Message(
        role='user',
        content = latest_msg,
        timestamp= datetime.ctime()
    )
    conversation.messages.append(latest_msg)
    response = send_message(conversation, provider)
    response_msg = Message(
        role='assistant',
        content = response["msg"],
        timestamp= datetime.ctime()
    )
    conversation.messages.append(response_msg)

    save_conversation(conversation)


