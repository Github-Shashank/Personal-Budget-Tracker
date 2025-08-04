# Personal-Budget-Tracker

# FUNCTIONS

1. add_expense()
2. add_income()
3. add_transaction(amount, category, transaction_mode)
4. load_data()
5. main()
6. save_data()
7. view_summary()
8. view_transactions()

# DATA

1. filename = 'budget_data.csv'
2. functions = {1: <function add_income>, 2: <function add_expense>, 3: <function view_transactions>, 4: <function view_summary>, 5: <function save_data>}
3. transactions = []

# FILE
https://github.com/Github-Shashank/Personal-Budget-Tracker/blob/main/personal_budget_tracker.py

# Example Output
```
No previous CSV data found. Starting fresh.

============ WELCOME TO PERSONAL BUDGET TRACKER ============

1. Add Income
2. Add Expense
3. View Transactions
4. View Summary
5. Save data
6. Quit

Enter your choice (1-6) :- 1

======================== Add Income ========================

Enter amount :- 40000
Enter category :- Salary

Data added ['2025-08-04 13:58:11'] Income :₹40000.0 Salary

Press Enter to continue... 

============ WELCOME TO PERSONAL BUDGET TRACKER ============

1. Add Income
2. Add Expense
3. View Transactions
4. View Summary
5. Save data
6. Quit

Enter your choice (1-6) :- 2

======================= Add Expense ========================

Enter amount :- 14000
Enter category :- Mobile

Data added ['2025-08-04 13:58:38'] Expense:₹14000.0 Mobile

Press Enter to continue...

============ WELCOME TO PERSONAL BUDGET TRACKER ============

1. Add Income
2. Add Expense
3. View Transactions
4. View Summary
5. Save data
6. Quit

Enter your choice (1-6) :- 3

==================== View Transactions =====================

['2025-08-04 13:58:11'] Income :₹40000.0 Salary
['2025-08-04 13:58:38'] Expense:₹14000.0 Mobile

Press Enter to continue...

============ WELCOME TO PERSONAL BUDGET TRACKER ============

1. Add Income
2. Add Expense
3. View Transactions
4. View Summary
5. Save data
6. Quit

Enter your choice (1-6) :- 4

======================= View Summary =======================

Total Income:   ₹40000.0
Total Expenses: ₹14000.0
Balance:        ₹26000.0

Press Enter to continue...  

============ WELCOME TO PERSONAL BUDGET TRACKER ============

1. Add Income
2. Add Expense
3. View Transactions
4. View Summary
5. Save data
6. Quit

Enter your choice (1-6) :- 5

Data saved successfully in CSV format.

Press Enter to continue...

============ WELCOME TO PERSONAL BUDGET TRACKER ============

1. Add Income
2. Add Expense
3. View Transactions
4. View Summary
5. Save data
6. Quit

Enter your choice (1-6) :- 6

Quitting Personal Budget Tracker
```
