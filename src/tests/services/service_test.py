import unittest
from entities.user import User
from entities.entry import Entry
from services.diary_service import (
    DiaryService,
    InvalidCredentialsError,
    UsernameExistsError
)


class FakeEntryRepository:
    def __init__(self, entries=None):
        self.entries = entries or []
    
    def find_all(self):
        return self.entries
    
    def find_by_username(self, username):
        user_entries = filter(
            lambda entry: entry.user and entry.user.username == username,
            self.entries)
        
        return list(user_entries)
    
    def create(self, entry):
        self.entries.append(entry)
        return entry
    
    def delete_entry(self, entry_id):
        new_entries = filter(lambda entry: entry.id != entry_id, self.entries)
        self.entries = list(new_entries)
        
    def delete_all(self):
        self.entries = []


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
            FakeUserRepository(),
            FakeEntryRepository()
        )
        self.user_testi = User("testi", "testi123")
        self.entry_a = Entry("testing a", "happy")
        self.entry_b = Entry("testing b", "sad")

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
    
    def test_create_entry(self):
        self.login_user(self.user_testi)
        self.diary_service.create_entry("testing", "euphoric")
        
        entries = self.diary_service.get_entries()
        
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].content, "testing")
        self.assertEqual(entries[0].emotion, "euphoric")
        self.assertEqual(entries[0].user.username, self.user_testi.username)
    
    def test_delete_entry(self):
        self.login_user(self.user_testi)
        self.diary_service.create_entry("testing", "happy")
        
        entries = self.diary_service.get_entries()
        self.assertEqual(len(entries), 1)
        
        self.diary_service.delete_entry(entries[0].id)
        
        entries = self.diary_service.get_entries()
        self.assertEqual(len(entries), 0)
        
    def test_get_entries(self):
        self.login_user(self.user_testi)
        
        self.diary_service.create_entry(
            self.entry_a.content, self.entry_a.emotion)

        self.diary_service.create_entry(
            self.entry_b.content, self.entry_b.emotion)

        entries = self.diary_service.get_entries()

        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0].content, self.entry_a.content)
        self.assertEqual(entries[1].emotion, self.entry_b.emotion)
