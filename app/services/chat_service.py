from app.storage.storage import load_current_conversation, save_conversation
from app.services.providers.provider import send_message
from app.models.message import Message
from datetime import datetime


def chat_model(latest_msg: str, provider: str):
    conversation = load_current_conversation()
    latest_msg = Message(
        role="user",
        content=latest_msg,
        timestamp=datetime.now()
    )
    conversation.messages.append(latest_msg)
    response = send_message(conversation, provider)
    response_msg = Message(
        role="assistant",
        content=response,
        timestamp=datetime.now()
    )
    conversation.messages.append(response_msg)

    save_conversation(conversation)
    return response
