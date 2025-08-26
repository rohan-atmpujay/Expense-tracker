import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

class Expense:
    def __init__(self, starting_amount=0.0, expense_name="", expense_category="", expense_amount=0.0):
        self.expense_name = expense_name
        self.expense_category = expense_category
        self.expense_amount = expense_amount
        self.starting_amount = starting_amount

    def set_starting_amount(self):
        self.starting_amount = float(input("Please enter the starting amount: "))

    def expense_details(self):
        self.expense_name = input("Enter expense name: ")
        self.expense_amount = float(input("Enter expense amount: "))
        categories = ["🍔 food", "🏠 house", "🎉 fun", "🤷 misc"]
        for index, value in enumerate(categories, start=1):
            print(f"{index}. {value}")

        choice = int(input("Please select your category (1-4): "))
        if 1 <= choice <= len(categories):
            self.expense_category = categories[choice - 1]  # store category name
        else:
            self.expense_category = "🤷 misc"  # default if invalid choice

    def save_files(self):
        with open('expense.txt', 'a', encoding="utf-8") as f:
            f.write(f"Expense: {self.expense_name} | Category: {self.expense_category} | Amount: ${self.expense_amount}\n")

    def show_expenses(self):
        print('-----All Expenses-----')
        try:
            with open('expense.txt', 'r', encoding="utf-8") as f:
                lines = f.readlines()
                if not lines:
                    print("No expense recorded yet.")
                else:
                    for index, line in enumerate(lines, start=1):
                        self.expense_name, self.expense_category, self.expense_amount = line.strip().split("|")
                        print(f"{index}. Expense: {self.expense_name} | Category: {self.expense_category} | Amount: ${self.expense_amount}\n")
        except FileNotFoundError:
            print("No expenses recorded yet.")

    def expense_summary(self):
        total_amount = 0.0
        try:
            with open('expense.txt', 'r', encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split('|')
                    if len(parts) == 3:
                        # Extract the amount string and clean it
                        amount_str = parts[2].replace("Amount: ", "").replace("$", "").strip()
                        total_amount += float(amount_str)
        except FileNotFoundError:
            print("No expenses recorded yet.")
        except ValueError as e:
            print(f"Error converting amount to float: {e}")

        remaining = self.starting_amount - total_amount
        print("\n📊 Expense Summary")
        print(f"💰 Starting Amount: ${self.starting_amount}")
        print(f"💸 Total Spent: ${total_amount}")
        print(f"✅ Remaining Balance: ${remaining}")

def main():
    expense = Expense()
    expense.set_starting_amount()
    # Set starting amount before recording expenses
    expense.expense_details()
    expense.save_files()
    expense.expense_summary()
    print("✅ Expense saved successfully!")

if __name__ == "__main__":
    main()
