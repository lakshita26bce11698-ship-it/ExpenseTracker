import datetime

class Expense:
    """Represents an individual expense entry."""
    def __init__(self, expense_id: int, title: str, category: str, amount: float, date_str: str = None):
        self.expense_id = expense_id
        self.title = title
        self.category = category.strip().capitalize()
        self.amount = float(amount)
        self.date_str = date_str if date_str else datetime.date.today().strftime("%Y-%m-%d")

    def to_dict(self) -> dict:
        """Converts object instance into a dictionary for JSON serialization."""
        return {
            "id": self.expense_id,
            "title": self.title,
            "category": self.category,
            "amount": self.amount,
            "date": self.date_str
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Creates an Expense object from a dictionary."""
        return cls(
            expense_id=data["id"],
            title=data["title"],
            category=data["category"],
            amount=data["amount"],
            date_str=data["date"]
        )