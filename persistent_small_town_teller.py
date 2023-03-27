import pickle

from small_town_teller import Person, Account, Bank


class PersistenceUtils:
    @staticmethod
    def write_pickle(data):
        pickle.dump(data, open('data.pickle', 'wb'))

    #   with open('data.pickle', 'wb') as file:
    #   (pickle.load(file))
    @staticmethod
    def load_pickle():
        return pickle.load(open('data.pickle', 'rb'))


# with open('data.pickle','rb') as file:
#     pickle.dump(Bank.accounts,file)

class Bank(Bank):
    def save_data(self):
        PersistenceUtils.write_pickle(self.accounts)

    def load_data(self):
        self.accounts = PersistenceUtils.load_pickle()
        for value in self.accounts:
            self.add_customer(self.accounts.get(value).owner)


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


    zc_bank.customers
    # {}
    zc_bank.accounts
    # {}
    zc_bank.save_data()
    zc_bank.load_data()
    print(zc_bank.customers)
    # {1: <persistent_small_town_teller.Person object at 0x1098e6a90>}
    print(zc_bank.accounts)
    # {1001: <persistent_small_town_teller.Account object at 0x1099e04d0>}
