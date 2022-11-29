import uuid
from datetime import datetime
from zoneinfo import ZoneInfo

class Entry:
    def __init__(self, content, emotion=None, user=None, entry_id=None):
        self.content = content
        self.emotion = emotion
        self.user = user
        self.id = entry_id or str(uuid.uuid4())
        self.date = datetime.now(ZoneInfo("EET")).strftime("%Y-%m-%d %H:%M")

