import json
from datetime import datetime
from pathlib import Path

from app.models.conversation import Conversation
from app.models.message import Message

DATA_FILE = Path("app/storage/data/data.json")


def _message_from_dict(message_data: dict) -> Message:
    timestamp = message_data.get("timestamp")
    if timestamp:
        timestamp = datetime.fromisoformat(timestamp)
    else:
        timestamp = datetime.now()

    return Message(
        role=message_data["role"],
        content=message_data["content"],
        timestamp=timestamp,
    )


def load_current_conversation() -> Conversation:
    if not DATA_FILE.exists():
        return Conversation(messages=[])

    raw_content = DATA_FILE.read_text(encoding="utf-8").strip()
    if not raw_content:
        return Conversation(messages=[])

    try:
        content = json.loads(raw_content)
    except json.JSONDecodeError:
        return Conversation(messages=[])

    messages = [_message_from_dict(message_data) for message_data in content.get("messages", [])]
    return Conversation(messages=messages)


def save_conversation(conversation: Conversation):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "messages": [
            {
                "role": message.role,
                "content": message.content,
                "timestamp": message.timestamp.isoformat(),
            }
            for message in conversation.messages
        ]
    }
    DATA_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print("Stored Conversation")
