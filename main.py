import csv
from datetime import datetime
from categories import list_nodes, tree_nodes, sort_by_category, sort_by_price, sort_by_date, sort_by_item
from budgetAndSpending import Budget

# Define the terminal menu function
def terminal_menu():
    budget_manager = None
    
    while True:
        print("\n==== Budget Tracker Menu ====")
        print("1. Set Budget")
        print("2. Sort")
        print("3. Check Budget")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            budget_amount = float(input("Enter your monthly budget amount: $"))
            budget_manager = Budget(budget_amount)
            print(f"Budget of ${budget_amount:.2f} has been set.")
        
        elif choice == "2":
            print("\n=== Sort Options ===")
            print("1. Sort by Category")
            print("2. Sort by Price")
            print("3. Sort by Date")
            print("4. Sort by Item")
            
            sort_choice = input("Select a sorting option (1-4): ")
            
            if sort_choice == "1":
                sort_by_category()
            elif sort_choice == "2":
                sort_by_price(tree_nodes)
            elif sort_choice == "3":
                sort_by_date()
            elif sort_choice == "4":
                sort_by_item()
            else:
                print("Invalid choice. Please select 1-4.")
        
        elif choice == "3":
            if budget_manager is None:
                print("Please set a budget first.")
            else:
                update_budget_with_transactions(budget_manager, list_nodes)
                budget_manager.display_status()
        
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid option. Please select 1-4.")

# Function to update the budget with transactions
def update_budget_with_transactions(budget_manager, transactions):
    for transaction in transactions:
        budget_manager.addSpending(transaction.price)

# Run the terminal menu
terminal_menu()
