from pathlib import Path
from entities.entry import Entry
from repositories.user_repository import user_repository
from config import ENTRIES_FILE_PATH


class EntryRepository:
    """Luokka, joka vastaa päiväkirjapostauksiin liittyvistä tietokantaoperaatioista."""

    def __init__(self, file_path):
        """Luokan konstruktori.

        Args:
            file_apth: Polku tiedostoon, johon postaukset tallennetaan.
        """

        self._file_path = file_path

    def find_all(self):
        """Palauttaa kaikki päiväkirjapostaukset.

        Returns:
            Listan Entry-olioita.
        """

        return self._read()

    def find_by_username(self, username):
        """Palauttaa käyttäjän päiväkirjapostaukset.

        Args:
            username: Käyttäjä, jonka postaukset palautetaan.
        Returns:
            Palauttaa listan Entry-olioita.
        """

        entries = self.find_all()
        user_entries = filter(
            lambda entry: entry.user and entry.user.username == username, entries)

        return list(user_entries)

    def _ensure_file_exist(self):
        Path(self._file_path).touch()

    def create(self, entry):
        """Tallentaa postauksen tietokantaan.

        Args:
            entry: Tallennettava postaus Entry-oliona.
        Returns:
            Tallennettu postaus Entry-oliona.
        """

        entries = self.find_all()
        entries.append(entry)
        self._write(entries)

        return entry
    
    def delete_entry(self, entry_id):
        """Poistaa tietyn postauksen.
        
        Args:
            entry_id: Poistettavan postauksen id.
        """
        
        entries = self.find_all()
        new_entries = filter(lambda entry: entry.id != entry_id, entries)
        self._write(new_entries)
        
    def delete_all(self):
        """Poistaa kaikki postaukset."""
        self._write([])

    def _read(self):
        entries = []
        self._ensure_file_exist()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                entry_id = parts[0]
                date = parts[1]
                content = parts[2]
                emotion = parts[3]
                username = parts[4]

                user = user_repository.find_by_username(
                    username) if username else None

                entries.append(
                    Entry(content, emotion, user, entry_id, date)
                )

        return entries

    def _write(self, entries):
        self._ensure_file_exist()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for entry in entries:
                username = entry.user.username if entry.user else ""
                row = f"{entry.id};{entry.date};{entry.content};{entry.emotion};{username}"
                file.write(row+"\n")


entry_repository = EntryRepository(ENTRIES_FILE_PATH)
