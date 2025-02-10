# Finance Tracker
transactions = []

def add_transaction():
    amount = float(input("Enter amount: "))
    t_type = input("Is it Income or Expense? ").strip().capitalize()

    if t_type not in ["Income", "Expense"]:
        print("Invalid type! Please enter 'Income' or 'Expense'.")
        return

    category = input("Enter category (e.g., Salary, Groceries, Rent): ").strip().capitalize()
    transactions.append({"amount": amount, "type": t_type, "category": category})
    print("Transaction recorded successfully!\n")

def view_summary():
    total_income = sum(t["amount"] for t in transactions if t["type"] == "Income")
    total_expense = sum(t["amount"] for t in transactions if t["type"] == "Expense")
    net_balance = total_income - total_expense

    print("\n===== Financial Summary =====")
    print(f"Total Income: ₹{total_income}")
    print(f"Total Expenses: ₹{total_expense}")
    print(f"Net Balance: ₹{net_balance}")
    print("============================\n")

while True:
    print("\n1. Add Transaction")
    print("2. View Summary")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_transaction()
    elif choice == "2":
        view_summary()
    elif choice == "3":
        print("Exiting... Have a great day!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
        
""""This Personal Finance Tracker is designed to help users manage their daily income and expenses efficiently. The program follows a structured approach, making it easy to use and understand.

How It Works
The tracker starts by initializing an empty list called transactions, which acts as a storage container for all financial records. Each transaction includes three key details:

Amount - The money involved in the transaction.
Type - Whether it is an Income (money earned) or an Expense (money spent).
Category - A label such as Salary, Groceries, Rent, or Utilities to classify the transaction.
Adding Transactions
When the user chooses to add a transaction, the program prompts them to enter the amount, specify if it is an Income or Expense, and categorize it. The input is validated, ensuring that only "Income" or "Expense" is accepted. If the user enters an incorrect type, the program notifies them and stops that transaction from being recorded.

Viewing Summary
If the user selects the View Summary option, the program calculates and displays:

Total Income - The sum of all transactions classified as income.
Total Expenses - The sum of all transactions classified as expenses.
Net Balance - The difference between total income and expenses, representing the remaining amount.
This gives the user a clear financial overview, showing how much money they have earned, spent, and saved.

Menu System & User Interaction
The program runs in a continuous loop, repeatedly displaying a menu with three options:

Add a Transaction
View Financial Summary
Exit the Program
The loop ensures that the user can keep adding transactions or check their summary until they decide to exit. If the user selects "Exit," the program stops running gracefully.

Why This Approach?
This structure ensures that the tracker is simple, efficient, and user-friendly. It allows users to quickly record transactions, get an instant financial summary, and make informed decisions about their money. Additionally, the modular design of the program makes it easy to expand and integrate new features like data storage or graphical reports in the future.

In summary, this Personal Finance Tracker provides a basic yet effective solution for managing finances, making it a useful tool for anyone looking to keep track of their expenses and savings."""