import uuid
from datetime import datetime


class Entry:
    def __init__(self, content, emotion=None, user=None, entry_id=None, date=None):
        self.content = content
        self.emotion = emotion
        self.user = user
        self.id = entry_id or str(uuid.uuid4())
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M")
