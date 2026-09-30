import datetime

class Validator:
    """Validates user input across all operations."""
    
    @staticmethod
    def validate_amount(val: str) -> float:
        """Validates positive float amounts."""
        amount = float(val)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return round(amount, 2)

    @staticmethod
    def validate_date(date_text: str) -> str:
        """Validates YYYY-MM-DD date format."""
        if not date_text.strip():
            return datetime.date.today().strftime("%Y-%m-%d")
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
        return date_text