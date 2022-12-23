from entities.entry import Entry
from entities.user import User


from repositories.entry_repository import (
    entry_repository as default_entry_repository
)

from repositories.user_repository import (
    user_repository as default_user_repository
)


class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class DiaryService:
    """Luokka sovelluslogiikkaa varten."""

    def __init__(
        self,
        user_repository=default_user_repository,
        entry_repository=default_entry_repository
    ):
        """Luokan konstruktori. Luo uuden palvelun sovelluslogiikkaa varten.

        Args:
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """

        self._user = None
        self._user_repository = user_repository
        self._entry_repository = entry_repository

    def logout(self):
        """Kirjaa käyttäjän ulos."""
        self._user = None

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa salasanaa.
        Raises:
            InvalidCredentialsError:
                Virhetilanne, jossa käyttäjätunnus ja salasana eivät täsmää.
        Returns:
            Sisäänkirjautunut käyttäjä User-oliona.
        """

        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user

    def register(self, username, password, login=True):
        """Luo uuden käyttäjän.

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa salasanaa.
            login:
                Vapaaehtoinen, oletusarvoltaan True.
                Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen.
        Raises:
            UsernameExistsError:
                Virhetilanne, jossa käyttäjätunnus on jo olemassa.
        Returns:
            Palauttaa luodun käyttäjän User-oliona.
        """

        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")
        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user
        return user

    def get_current_user(self):
        """Palauttaa kirjautuneena olevan käyttäjän.

        Returns:
            Palauttaa kirjautuneena olevan käyttäjän User-oliona.
        """

        return self._user

    def get_users(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa kaikki käyttäjät User-olioiden listana.
        """

        return self._user_repository.find_all()

    def create_entry(self, content, emotion):
        """Luo uuden päiväkirjapostauksen.

        Args:
            content: Merkkijonoarvo, joka kuvaa käyttäjän päivää.
            emotion: Merkkijonoarvo, joka kuvaa käyttäjän tunnetilaa.
        Returns:
            Luotu postaus Entry-olion muodossa.
        """

        entry = Entry(content=content, emotion=emotion, user=self._user)
        return self._entry_repository.create(entry)

    def delete_entry(self, entry_id):
        """Poistaa tietyn postauksen.

        Args:
            entry_id: Merkkijonoarvo, joka kuvaa postauksen id:tä.
        """

        self._entry_repository.delete_entry(entry_id)

    def get_entries(self):
        """Palauttaa kirjautuneen käyttäjän päiväkirjapostaukset.

        Returns:
            Palauttaa kirjautuneen käyttäjän päiväkirjapostaukset Entry-olioiden listana.
            Jos kirjautunutta käyttäjää ei ole, palauttaa tyhjän listan.
        """

        if not self._user:
            return []

        return self._entry_repository.find_by_username(self._user.username)


diary_service = DiaryService()
