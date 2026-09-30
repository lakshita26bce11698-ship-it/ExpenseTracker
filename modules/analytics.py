from typing import List, Dict
from modules.models import Expense

class ExpenseAnalytics:
    """Module responsible for analytics and computations."""

    @staticmethod
    def total_spending(expenses: List[Expense]) -> float:
        """Calculates total expense amount."""
        return sum(e.amount for e in expenses)

    @staticmethod
    def category_breakdown(expenses: List[Expense]) -> Dict[str, float]:
        """Generates sum total grouped by category."""
        breakdown = {}
        for item in expenses:
            breakdown[item.category] = breakdown.get(item.category, 0.0) + item.amount
        return breakdown