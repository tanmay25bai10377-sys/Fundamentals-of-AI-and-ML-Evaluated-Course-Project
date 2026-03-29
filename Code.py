# Fundamentals-of-AI-and-ML-Evaluated-Course-Project
# Student Expense Tracker
# Student Expense Tracker

expenses = []

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, Study, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    
    expenses.append(expense)
    print("✅ Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    
    print("\n📊 All Expenses:")
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['description']}")
    print()

def total_spending():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Spending: ₹{total}\n")

def category_summary():
    summary = {}
    
    for exp in expenses:
        category = exp["category"]
        summary[category] = summary.get(category, 0) + exp["amount"]
    
    print("\n📂 Category-wise Spending:")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")
    print()

def menu():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category Summary")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_spending()
        elif choice == '4':
            category_summary()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

menu()
