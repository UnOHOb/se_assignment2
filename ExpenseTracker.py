import json

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input("Enter category (e.g., Food, Transport, Rent): ").capitalize()

    # Create the entry
    new_entry = {
        "date": date,
        "amount": amount,
        "category": category
    }

    # Load existing data or start a new list
    try:
        with open("expenses.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    # Append and save
    data.append(new_entry)
    with open("expenses.json", "w") as f:
        json.dump(data, f, indent=4)
    
    print("Expense saved successfully!")

if __name__ == "__main__":
    while True:
        choice = input("\n1. Add Expense\n2. Exit\nSelect: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            break
