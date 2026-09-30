from typing import List
from modules.models import Expense
from modules.storage import StorageHandler
from modules.analytics import ExpenseAnalytics

class TrackerService:
    """Primary service coordinating CRUD operations and processing."""

    def __init__(self):
        self.storage = StorageHandler()
        self.expenses: List[Expense] = self.storage.load_expenses()

    def _generate_id(self) -> int:
        return max([e.expense_id for e in self.expenses], default=0) + 1

    def add_expense(self, title: str, category: str, amount: float, date_str: str) -> Expense:
        new_id = self._generate_id()
        expense = Expense(new_id, title, category, amount, date_str)
        self.expenses.append(expense)
        self.storage.save_expenses(self.expenses)
        return expense

    def get_all_expenses(self) -> List[Expense]:
        return self.expenses

    def delete_expense(self, expense_id: int) -> bool:
        initial_length = len(self.expenses)
        self.expenses = [e for e in self.expenses if e.expense_id != expense_id]
        if len(self.expenses) < initial_length:
            self.storage.save_expenses(self.expenses)
            return True
        return False

    def get_analytics(self) -> dict:
        return {
            "total": ExpenseAnalytics.total_spending(self.expenses),
            "categories": ExpenseAnalytics.category_breakdown(self.expenses)
        }