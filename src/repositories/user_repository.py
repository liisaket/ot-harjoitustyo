from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """Luokka, joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista."""

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection = Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def create(self, user):
        """Tallentaa käyttäjän tietokantaan.

        Args:
            user: Tallennettava käyttäjä User-oliona.
        Returns:
            Palauttaa tallennetun käyttäjän User-oliona.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()
        return user

    def find_all(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa listan kaikista käyttäjistä User-olioina.
        """

        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return [User(row["username"], row["password"]) for row in rows]

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen perusteella.

        Args:
            username: Käyttäjätunnus, jonka perusteella käyttäjä haetaan.
        Returns:
            Palauttaa käyttäjän User-oliona, jos haettu käyttäjätunnus löytyy tietokannasta.
            Muussa tapauksessa palauttaa None.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )
        row = cursor.fetchone()
        return User(row["username"], row["password"]) if row else None

    def delete_all(self):
        """Poistaa kaikki käyttäjät tietokannasta."""
        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
