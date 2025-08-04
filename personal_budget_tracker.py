import csv                              # To save data in csv file
from datetime import datetime           # To get time stamp of trnsaction

transactions = []
filename = "budget_data.csv"            # Set your file location to save data

# To add income
def add_income():
    print("\n======================== Add Income ========================\n")
    amount = int(input("Enter amount :- "))
    category = input("Enter category :- ")
    add_transaction(float(amount),category,"Income")

# To add expense
def add_expense():
    print("\n======================= Add Expense ========================\n")
    amount = int(input("Enter amount :- "))
    category = input("Enter category :- ")
    add_transaction(float(amount),category,"Expense")

# To add transaction
def add_transaction(amount,category,transaction_mode):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction_data = {
        "time_stamp":[time_stamp],
        "transaction_mode": transaction_mode,
        "amount": amount,
        "category": category
    }
    print()
    print(f"Data added {[time_stamp]} {transaction_mode:<7}:₹{amount} {category}\n")
    transactions.append(transaction_data)

# To show all transactions
def view_transactions():
    print("\n==================== View Transactions =====================\n")
    if not transactions:
        print("There is no transactions yet")
    else:
        for data in transactions:
            print(f"{data['time_stamp']} {data['transaction_mode']:<7}:{'₹'+str(data['amount']):>7} {data['category']:<10}")
    print()

# To show summary
def view_summary():
    print("\n======================= View Summary =======================\n")
    income = sum(t['amount'] for t in transactions if t['transaction_mode'] == "Income")
    expenses = sum(t['amount'] for t in transactions if t['transaction_mode'] == "Expense")
    balance = income - expenses
    print(f"Total Income:   ₹{income}")
    print(f"Total Expenses: ₹{expenses}")
    print(f"Balance:        ₹{balance}")
    print()

# To save data to file
def save_data():
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time_stamp", "transaction_mode", "amount", "category"])
        for t in transactions:
            writer.writerow([t["time_stamp"], t["transaction_mode"], t["amount"], t["category"]])
    print("\nData saved successfully in CSV format.\n")

# To load data from file
def load_data():
    # Creates file if not available
    global transactions
    transactions = []
    try:
        # Open file to read
        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                if len(row) == 4:

                    time_stamp,transaction_mode, amount, category = row
                    amount_value = float(amount)
                    transactions.append({
                        "time_stamp": time_stamp,
                        "transaction_mode": transaction_mode,
                        "amount": amount_value,
                        "category": category
                    })

        print("\nData loaded successfully from CSV file.")

    except FileNotFoundError:
        transactions = []
        print("\nNo previous CSV data found. Starting fresh.")

functions = {1:add_income, 2:add_expense, 3:view_transactions, 4:view_summary, 5:save_data}

def main():

    load_data()
    status = "Saved"

    while True:
        print("""
============ WELCOME TO PERSONAL BUDGET TRACKER ============

1. Add Income
2. Add Expense
3. View Transactions
4. View Summary
5. Save data
6. Quit
""")    
        try:
            choice = int(input("Enter your choice (1-6) :- "))
            if choice == 6:
                if status == "Unsaved":
                    save_choice = input("\nYou have unsaved changes. Save before quitting? (y/n): ").lower()
                    if save_choice == 'y':
                        save_data()
                        print("\nQuitting Personal Budget Tracker\n")
                    else:
                        print("\nQuitting Personal Budget Tracker without saving")
                    break
                else:
                    print("\nQuitting Personal Budget Tracker\n")
                    break
            elif choice in [1,2]:
                status = "Unsaved"
            elif choice == 5:
                status = "Saved"
            if choice in functions:
                functions[choice]()
        except Exception as e:
            print(f"An error occured: {e}")
            print("""\nNote:
1. Choice should be between 1 and 6
2. Amount should be entered as an integer
3. Category should be a string\n""")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()