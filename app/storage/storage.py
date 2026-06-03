
from models.message import Message
from models.conversation import Conversation


def load_current_conversation()->Conversation:

    file = open("data.json","r")
    content = file.read()

    messages = []

    for message_data in content["messages"]:

        message = Message(
            role = message_data["role"],
            content = message_data["content"]
        )
        messages.append(message)

    return Conversation(messages=messages)


def save_conversation(conversation : Conversation):
    with open("data.json", "a", encoding="utf-8") as f:
        f.write(conversation)
    print("Stored Conversation")