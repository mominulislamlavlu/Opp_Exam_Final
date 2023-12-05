class Bank:
    def __init__(self):
        self.accounts = {} 
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, account_number):
        self.accounts[account_number] = {"balance": 0, "loan": 0, "transactions": []}

    def deposit(self, account_number, amount):
        self.accounts[account_number]["balance"] += amount
        self.total_balance += amount
        self.accounts[account_number]["transactions"].append(f"Deposited ={amount} TK")

    def withdraw(self, account_number, amount):
        if self.accounts[account_number]["balance"] >= amount:
            self.accounts[account_number]["balance"] -= amount
            self.total_balance -= amount
            self.accounts[account_number]["transactions"].append(f"Withdrew ={amount} TK")
        else:
            print("Bankrupt: Insufficient funds!")

    def transfer(self, from_account, to_account, amount):
        if self.accounts[from_account]["balance"] >= amount:
            self.accounts[from_account]["balance"] -= amount
            self.accounts[to_account]["balance"] += amount
            self.accounts[from_account]["transactions"].append(f"Transferred {amount} TK to {to_account}")
            self.accounts[to_account]["transactions"].append(f"Received {amount} TK from {from_account}")
        else:
            print("Bankrupt: Insufficient funds!")

    def check_balance(self, account_number):
        return self.accounts[account_number]["balance"]

    def check_transaction_history(self, account_number):
        return self.accounts[account_number]["transactions"]

    def take_loan(self, account_number):
        if self.loan_feature_enabled:
            total_amount = 2 * self.accounts[account_number]["balance"]
            self.accounts[account_number]["loan"] += total_amount
            self.total_loan_amount += total_amount
            self.accounts[account_number]["transactions"].append(f"Took a loan of {total_amount} TK")
        else:
            print("Loan feature is currently disabled by the admin.")

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, account_number):
        self.bank.create_account(account_number)

    def check_total_balance(self):
        return self.bank.total_balance

    def check_total_loan_amount(self):
        return self.bank.total_loan_amount

    def toggle_loan_feature(self, enable):
        self.bank.loan_feature_enabled = enable




bank = Bank()
admin = Admin(bank)


admin.create_account("MOMINUL")
admin.create_account("MARUF")

bank.deposit("MOMINUL", 1000)
bank.transfer("MOMINUL", "MARUF", 500)
bank.withdraw("MARUF", 200)


print(admin.check_total_balance())  
print(admin.check_total_loan_amount())  


admin.toggle_loan_feature(False)


bank.take_loan("MOMINUL")

