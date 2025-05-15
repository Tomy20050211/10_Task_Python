wallet = {}

def add_expense():
    category = input("Category: ").title()
    try:
        amount = float(input("Amount: $"))
        wallet[category] = wallet.get(category, 0) + amount
        print(f"Added ${amount:.2f} to {category}.")
    except:
        print("Invalid amount.")

def total_spent():
    print(f"Total spent: ${sum(wallet.values()):.2f}")

def expense_percentages():
    total = sum(wallet.values())
    if total == 0:
        print("No expenses yet.")
        return
    for cat, amt in wallet.items():
        print(f"{cat}: ${amt:.2f} ({amt / total * 100:.1f}%)")


while True:
    print("\n1. Add expense\n2. View total spent\n3. View percentages\n4. Exit")
    option = input("Choose an option: ")
    if option == '1':
        add_expense()
    elif option == '2':
        total_spent()
    elif option == '3':
        expense_percentages()
    elif option == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
