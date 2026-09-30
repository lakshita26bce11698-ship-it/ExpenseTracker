import json
import os
from typing import List
from modules.models import Expense

class StorageHandler:
    """Handles JSON file reads and writes."""
    
    def __init__(self, filepath: str = "data/expenses.json"):
        self.filepath = filepath
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Creates data directory and empty storage file if missing."""
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump([], f)

    def load_expenses(self) -> List[Expense]:
        """Loads all expenses from JSON storage."""
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
                return [Expense.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_expenses(self, expenses: List[Expense]) -> bool:
        """Saves current expense collection back to JSON file."""
        try:
            with open(self.filepath, 'w') as f:
                json.dump([e.to_dict() for e in expenses], f, indent=4)
            return True
        except Exception:
            return False