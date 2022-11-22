from entities.user import User
from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def create(self, user):
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return [User(row["username"], row["password"]) for row in rows]
    
    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute("delete from users")

        self._connection.commit()


user_repository = UserRepository(get_database_connection())