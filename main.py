from modules.tracker_service import TrackerService
from modules.validator import Validator

def display_menu():
    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Analytics & Summary")
    print("4. Delete Expense")
    print("5. Exit")
    print("=====================================")

def main():
    service = TrackerService()
    
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            try:
                title = input("Enter expense title: ").strip()
                if not title:
                    print("Error: Title cannot be empty.")
                    continue
                category = input("Enter category (e.g., Food, Rent, Travel): ").strip()
                amount_str = input("Enter amount ($): ").strip()
                amount = Validator.validate_amount(amount_str)
                date_input = input("Enter date (YYYY-MM-DD) [Leave blank for today]: ").strip()
                valid_date = Validator.validate_date(date_input)
                
                exp = service.add_expense(title, category, amount, valid_date)
                print(f"\n[Success] Expense ID {exp.expense_id} added successfully!")
            except ValueError as e:
                print(f"[Input Error] {e}")

        elif choice == '2':
            expenses = service.get_all_expenses()
            if not expenses:
                print("\nNo expenses logged yet.")
            else:
                print("\nID  | Date       | Category    | Amount ($) | Title")
                print("-" * 55)
                for e in expenses:
                    print(f"{e.expense_id:<3} | {e.date_str} | {e.category:<11} | {e.amount:<10.2f} | {e.title}")

        elif choice == '3':
            analytics = service.get_analytics()
            print("\n=== EXPENSE SUMMARY ===")
            print(f"Total Expenditure: ${analytics['total']:.2f}")
            print("\nBreakdown by Category:")
            for cat, amt in analytics['categories'].items():
                print(f"  - {cat}: ${amt:.2f}")

        elif choice == '4':
            try:
                exp_id = int(input("Enter Expense ID to delete: "))
                if service.delete_expense(exp_id):
                    print(f"\n[Success] Expense ID {exp_id} removed.")
                else:
                    print(f"\n[Error] Expense ID {exp_id} not found.")
            except ValueError:
                print("[Input Error] Please enter a valid numerical ID.")

        elif choice == '5':
            print("\nThank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please choose an option between 1 and 5.")

if __name__ == "__main__":
    main()