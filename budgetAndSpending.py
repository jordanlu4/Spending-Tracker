import csv
from datetime import datetime
from categories import list_nodes

class Budget:
    def __init__(self, budget: float):  # Set a budget
        self.budget = budget
        self.remainingBudget = budget
        self.spent = 0

    def addSpending(self, amount):  # Add spending 
        self.remainingBudget -= amount
        self.spent += amount
        # print(f"Added spending: ${amount:.2f}. Remaining budget: ${self.remainingBudget:.2f}.")

    def getRemainingBudget(self):
        return self.remainingBudget

    def getSpent(self):
        return self.spent

    def display_status(self):
        print(f"Total Budget: ${self.budget:.2f}")
        print(f"Total Spent: ${self.spent:.2f}")
        if self.remainingBudget < 0:
            print(f"You're ${abs(self.remainingBudget):.2f} over budget! Cut back on spending.")
        else:
            print(f"Remaining Budget: ${self.remainingBudget:.2f}")
    
def update_budget_with_transactions(budget_manager, transactions):
    """Updates the budget based on a list of transactions (list_nodes)."""
    for transaction in transactions:
        budget_manager.addSpending(transaction.price)


# budget = Budget(1000)
# update_budget_with_transactions(budget, list_nodes)
# budget.display_status()
