class Transaction:
    def __init__(self, ttype, amount, description, category):
        self.ttype = ttype
        self.amount = -abs(amount) if ttype == "expense" else abs(amount)
        self.description = description
        self.category = category

    def __str__(self):
        return f"{self.ttype.capitalize()}: ${abs(self.amount)} | {self.description} | {self.category.capitalize()}"

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.total_balance = 0

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.total_balance += transaction.amount
        print(f"{transaction} has been added to the Finance Tracker!")

    def get_balance(self):
        print(f"Total Balance: ${self.total_balance} AUD")

    def get_income(self):
        total_income = sum(t.amount for t in self.transactions if t.ttype == "income")
        print(f"Total Income: ${total_income} AUD")

    def get_expense(self):
        total_expense = sum(abs(t.amount) for t in self.transactions if t.ttype == "expense")
        print(f"Total Expense: ${total_expense} AUD")

    def get_savings_percentage(self):
        total_income = sum(t.amount for t in self.transactions if t.ttype == "income")
        if total_income == 0:
            print("Savings Percentage: No income recorded, cannot calculate savings percentage.")
            return
        savings_percentage = (self.total_balance / total_income) * 100
        print(f"Savings Percentage: {savings_percentage:.2f}%")

    def show_all_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def get_totals_by_Category(self, category):
        total_by_category = 0
        for transaction in self.transactions:
            if transaction.category.lower() == category.lower():  # Case-insensitive match
                total_by_category += transaction.amount
        if total_by_category == 0:
            print(f"No transactions found for category '{category}'.")
        else:
            print(f"Transactions for Category '{category}' total to '${total_by_category:.2f}'")



# Testing
t1 = Transaction("income", 3200, "bonus", "cat1")
t2 = Transaction("income", 9299, "salary", "cat1")
t3 = Transaction("expense", 7023, "macbook pro", "cat2")
ft1 = FinanceTracker()

ft1.add_transaction(t1)
ft1.get_balance()

ft1.add_transaction(t2)
ft1.get_balance()

ft1.add_transaction(t3)
ft1.get_balance()

ft1.get_income()
ft1.get_expense()
ft1.get_savings_percentage()
ft1.show_all_transactions()

ft1.get_totals_by_Category("cat1")
