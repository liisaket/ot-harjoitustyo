import unittest
from entities.user import User
from services.diary_service import (
    DiaryService,
    InvalidCredentialsError,
    UsernameExistsError
)

class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def create(self, user):
        self.users.append(user)
        return user

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        found_users = filter(
            lambda user: user.username == username,
            self.users
        )
        found_users_list = list(found_users)
        return found_users_list[0] if len(found_users_list) > 0 else None

    def delete_all(self):
        self.users = []

class TestDiaryService(unittest.TestCase):
    def setUp(self):
        self.diary_service = DiaryService(
            FakeUserRepository()
        )
        self.user_testi = User("testi", "testi123")
    
    def login_user(self, user):
        self.diary_service.register(user.username, user.password)
    
    def test_valid_login(self):
        self.diary_service.register(
            self.user_testi.username,
            self.user_testi.password
        )
        user = self.diary_service.login(
            self.user_testi.username,
            self.user_testi.password
        )
        self.assertEqual(user.username, self.user_testi.username)
    
    def test_invalid_login(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.diary_service.login("invalid", "credentials")
        )
    
    def test_get_current_user(self):
        self.login_user(self.user_testi)
        current_user = self.diary_service.get_current_user()
        self.assertEqual(current_user.username, self.user_testi.username)
    
    def test_valid_register(self):
        username = self.user_testi.username
        password = self.user_testi.password
        
        self.diary_service.register(username, password)
        
        users = self.diary_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)
    
    def test_invalid_register(self):
        username = self.user_testi.username

        self.diary_service.register(username, "new")

        self.assertRaises(
            UsernameExistsError,
            lambda: self.diary_service.register(username, "random")
        )
