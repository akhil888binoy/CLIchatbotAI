from dataclasses import dataclass
from app.models.message import Message


@dataclass
class Conversation:
    messages: list[Message]
