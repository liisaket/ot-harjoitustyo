import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_testi = User("testi", "testi123")
        self.user_touko = User("touko", "touko123")

    def test_create(self):
        user_repository.create(self.user_testi)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_testi.username)

    def test_find_all(self):
        user_repository.create(self.user_testi)
        user_repository.create(self.user_touko)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_testi.username)
        self.assertEqual(users[1].username, self.user_touko.username)

    def test_find_by_username(self):
        user_repository.create(self.user_testi)
        user = user_repository.find_by_username(self.user_testi.username)
        self.assertEqual(user.username, self.user_testi.username)
