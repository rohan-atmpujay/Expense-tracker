import sqlite3

DB_FILE = 'Expense_tracker.db'
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Expense_tracker(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    expense_amount INTEGER
)""")
conn.commit()


class Expense_tracker:
    def __init__(self):
        pass
        
    def list_expense(self):
        print('-----------------Expense List-----------------')
        cursor.execute("SELECT * FROM Expense_tracker")
        rows = cursor.fetchall()
        if not rows:
            print("❌ Expense list is empty.")
            return

        print(f"{'S.No':<5} {'ID':<5} {'Name':<20} {'Category':<15} {'Amount':<10}")
        print("-" * 60)
        for i, row in enumerate(rows, start=1):
            print(f"{i:<5} {row[0]:<5} {row[1]:<20} {row[2]:<15} {row[3]:<10}")

    
    def add_expense(self):
        name = input('Expense name: ')
        category = input('Expense category: ')
        try:
            amount = int(input('Expense amount: '))
        except ValueError:
            print('❌ Must be a positive number')
            return
        cursor.execute(
            'INSERT INTO Expense_tracker(name, category, expense_amount) VALUES (?, ?, ?)',
            (name, category, amount)
        )
        conn.commit()
        print("✅ Expense added successfully!")
    
    def edit_expense(self):
        self.list_expense()
        try:
            exp_id = int(input("Enter Expense ID to edit: "))
        except ValueError:
            print("❌ Invalid ID.")
            return
        
        cursor.execute('SELECT * FROM Expense_tracker WHERE id = ?', (exp_id,))
        row = cursor.fetchone()
        if not row:
            print("❌ Expense not found")
            return

        new_name = input(f'Enter new name [{row[1]}]: ') or row[1]
        new_category = input(f'Enter new category [{row[2]}]: ') or row[2]
        new_amount_input = input(f"Enter new amount [{row[3]}]: ")
        try:
            new_amount = int(new_amount_input) if new_amount_input else row[3]
        except ValueError:
            print('❌ Amount must be a number')
            return
        
        cursor.execute(
            'UPDATE Expense_tracker SET name = ?, category = ?, expense_amount = ? WHERE id = ?',
            (new_name, new_category, new_amount, exp_id)
        )
        conn.commit()
        print("✅ Expense updated successfully!")
        
    def delete_expense(self):
        try:
            exp_id = int(input("Enter Expense ID to delete: "))
        except ValueError:
            print("❌ Invalid ID.")
            return
        
        cursor.execute('SELECT * FROM Expense_tracker WHERE id = ?', (exp_id,))
        row = cursor.fetchone()
        if not row:
            print('❌ Expense not found')
            return
        
        cursor.execute('DELETE FROM Expense_tracker WHERE id = ?', (exp_id,))
        conn.commit()
        print("🗑️ Expense deleted successfully!")


def main():
    expense_tracker = Expense_tracker()
    
    while True:
        print('\n=== Expense Tracker with DB ===')
        print('1. List Expenses')
        print('2. Add Expense')
        print('3. Edit Expense')
        print('4. Delete Expense')
        print('5. Exit')
        choice = input('Please enter a choice (1-5): ')
        
        if choice == '1':
            expense_tracker.list_expense()
        elif choice == '2':
            expense_tracker.add_expense()
        elif choice == '3':
            expense_tracker.edit_expense()
        elif choice == '4':
            expense_tracker.delete_expense()
        elif choice == '5':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
