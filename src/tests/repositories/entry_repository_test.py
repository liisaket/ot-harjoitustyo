import unittest
from repositories.entry_repository import entry_repository
from repositories.user_repository import user_repository
from entities.entry import Entry
from entities.user import User


class TestEntryRepository(unittest.TestCase):
    def setUp(self):
        entry_repository.delete_all()
        user_repository.delete_all()

        self.entry_a = Entry("testing a", "happy")
        self.entry_b = Entry("testing b", "sad")
        self.user_testi = User("testi", "testi123")
        self.user_touko = User("touko", "touko123")

    def test_create(self):
        entry_repository.create(self.entry_a)
        entries = entry_repository.find_all()

        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].content, self.entry_a.content)

    def test_find_all(self):
        entry_repository.create(self.entry_a)
        entry_repository.create(self.entry_b)
        entries = entry_repository.find_all()

        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0].content, self.entry_a.content)
        self.assertEqual(entries[1].content, self.entry_b.content)

    def test_find_by_username(self):
        testi = user_repository.create(self.user_testi)
        touko = user_repository.create(self.user_touko)

        entry_repository.create(
            Entry(content="testing a", emotion="happy", user=testi))
        entry_repository.create(
            Entry(content="testing b", emotion="sad", user=touko))

        testi_entries = entry_repository.find_by_username(
            self.user_testi.username)
        self.assertEqual(len(testi_entries), 1)
        self.assertEqual(testi_entries[0].content, "testing a")

        touko_entries = entry_repository.find_by_username(
            self.user_touko.username)
        self.assertEqual(len(touko_entries), 1)
        self.assertEqual(touko_entries[0].content, "testing b")

    def test_delete_entry(self):
        entry = entry_repository.create(self.entry_a)
        entries = entry_repository.find_all()

        self.assertEqual(len(entries), 1)
        entry_repository.delete_entry(entry.id)

        entries = entry_repository.find_all()
        self.assertEqual(len(entries), 0)
