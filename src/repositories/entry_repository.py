from pathlib import Path
from entities.entry import Entry
from repositories.user_repository import user_repository
from config import ENTRIES_FILE_PATH

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
        pass
        


entry_repository = EntryRepository(ENTRIES_FILE_PATH)
