import uuid
from datetime import datetime


class Entry:
    """Yksittäistä päiväkirjapostausta kuvaava luokka.

    Attributes:
        content: Merkkijonoarvo, joka kuvaa käyttäjän päivää.
        emotion: Merkkijonoarvo, joka kuvaa käyttäjän tunnetilaa.
        user: User-olio, joka kuvaa postauksen omistajaa.
        entry_id: Merkkijonoarvo, joka kuvaa postauksen id:tä.
        date: Merkkijonoarvo, joka kuvaa postauksen luomispäivämäärää.
    """

    def __init__(self, content, emotion, user=None, entry_id=None, date=None):
        """Luokan konstruktori. Luo uuden postauksen.

        Args:
            content: Merkkijonoarvo, joka kuvaa käyttäjän päivää.
            emotion: Merkkijonoarvo, joka kuvaa käyttäjän tunnetilaa.
            user:
                Vapaaehtoinen, oletusarvoltaan None.
                User-olio, joka kuvaa postauksen omistajaa.
            entry_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joka kuvaa postauksen id:tä.
            date:
                Vapaaehtoinen, oletusarvoltaan generoitu datetime-olio.
                Merkkijonoarvo, joka kuvaa postauksen luomispäivämäärää. 
        """
        self.content = content
        self.emotion = emotion
        self.user = user
        self.id = entry_id or str(uuid.uuid4())
        self.date = date or datetime.now().strftime("%d-%m-%Y %H:%M")
