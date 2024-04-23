
from dataclasses import dataclass
from typing import List
from datetime import datetime

@dataclass
class Event:
    timestamp: datetime
    data: str

@dataclass
class Job:
    status: str
    events: List[Event]
    result: str