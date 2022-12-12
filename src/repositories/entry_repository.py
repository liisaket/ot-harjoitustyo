from pathlib import Path
from entities.entry import Entry
from repositories.user_repository import user_repository
from confid import ENTRIES_FILE_PATH

class EntryRepository:
    """Luokka, joka vastaa päiväkirjapostauksiin liittyvistä tietokantaoperaatioista."""
    def __init__(self, file_path):
        """Luokan konstuktori.
        
        Args:
            file_apth: Polku tiedostoon, johon postaukset tallennetaan.
        """

        self._file_path = file_path
    
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
                username =  entry.user.username if entry.user else ""
                row = f"{entry.id};{entry.date};{entry.content};{entry.emotion};{username}"
                file.write(row+"\n")


entry_repository = EntryRepository(ENTRIES_FILE_PATH)
