# CLI Expense Tracker

A modular Python Command Line Application designed to manage personal financial expenses.

## Features
- Record expenses with custom titles, amounts, categories, and dates.
- Persist data locally in JSON format (`data/expenses.json`).
- View comprehensive list of all entries.
- Category-wise aggregate summaries and analytics.
- Input validation and exception handling.

## Project Structure
```text
ExpenseTracker/
├── main.py
├── README.md
└── modules/
    ├── __init__.py
    ├── models.py
    ├── validator.py
    ├── storage.py
    ├── analytics.py
    └── tracker_service.py
