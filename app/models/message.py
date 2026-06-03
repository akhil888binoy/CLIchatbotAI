from dataclasses import dataclass
import datetime


@dataclass
class Message:
    role:str
    content : str
    timestamp: datetime.datetime


