import pickle

class Person:
    def __init__(self, identification, first_name, last_name):
        self.id = identification
        self.firstname = first_name
        self.lastname = last_name

class Account:
    def __init__(self, ac_number, ac_type, ac_owner):
        self.number = ac_number
        self.type = ac_type
        self.owner = ac_owner
        self.balance = 0

class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, person: Person):
        full_name = person.firstname + " " + person.lastname
        self.customers[person.id] = full_name

    def add_account(self, account: Account):
        self.accounts[account.number] = account

    def delete_account(self, identification, ac_number):
        del self.accounts[ac_number]

    def deposit(self, ac_number, deposit_amount):
        deposit_account = self.accounts.get(ac_number)
        deposit_account.balance += deposit_amount

    def withdrawal(self, ac_number, withdraw_amount):
        withdraw_account = self.accounts.get(ac_number)
        withdraw_account.balance -= withdraw_amount

    def balance_inquiry(self,ac_number):
        ac_balance = self.accounts.get(ac_number).balance
        print(ac_balance)
        return ac_balance

if __name__ == "__main__":
    zc_bank = Bank()
    bob = Person(1, "Bob", "Smith")
    zc_bank.add_customer(bob)
    bob_savings = Account(1001, "SAVINGS", bob)
    zc_bank.add_account(bob_savings)
    zc_bank.balance_inquiry(1001)
    # 0
    zc_bank.deposit(1001, 256.02)
    zc_bank.balance_inquiry(1001)
    # 256.02
    zc_bank.withdrawal(1001, 128)
    zc_bank.balance_inquiry(1001)
    # 128.02


