from entities.entry import Entry
from entities.user import User

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
        self._user = None

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user

    def register(self, username, password, login=True):
        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")
        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user
        return user

    def get_current_user(self):
        return self._user

    def get_users(self):
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


diary_service = DiaryService()
