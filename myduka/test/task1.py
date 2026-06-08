# TASK 1.Create a class called BankAccount with the attributes: - account number , balance , owner name , date opened
# 2.Add some behaviour to the above class using the methods: - deposit() - withdraw() - check_balance() -display_info() -close_account()
# 3.Create two BankAccount objects that can deposit , withdraw , check balance display info and close account


class Bankaccount:
    def __init__(self, Account_number, owner_name, balance, date_opened):
        self.account_number = Account_number
        self.owner_name = owner_name
        self.balance = balance
        self.date_opened = date_opened

    def deposit(self, amount):
        print(f"Depositing KSh {amount} to account {self.account_number}")
        self.balance += amount

    def withdraw(self, amount):
        print(f"Withdrawing KSh {amount} from account {self.account_number}")
        self.balance -= amount

    def check_balance(self):
        print(f"Account {self.account_number} balance: KSh {self.balance}")
    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: KSh {self.balance}")
        print(f"Date Opened: {self.date_opened}")
    def close_account(self):
        print(f"Closing account {self.account_number}")


#object1
Bankaccount1 = Bankaccount("119933", "mike", 1000000, (2020,5,20))
print(type(Bankaccount1))
print(Bankaccount1.account_number)
print(Bankaccount1.owner_name)
print(Bankaccount1.balance)
print(Bankaccount1.date_opened)
print(Bankaccount1.deposit(50000))
print(Bankaccount1.withdraw(20000))
print(Bankaccount1.balance)
print(Bankaccount1.display_info)
print(Bankaccount1.close_account)


#object2
Bankaccount2 = Bankaccount("100000", "Beth", 200000, (2022, 4, 8))
print("display info for Bankaccount2:")
Bankaccount2.display_info()
print()

print("depositing KSh 5000 to Bankaccount2:")
Bankaccount2.deposit(5000)
print()

print("withdrawing KSh 10000 from Bankaccount2:")
Bankaccount2.withdraw(10000)
print()

print("checking balance for Bankaccount2:")
Bankaccount2.check_balance()
print()

print("closing Bankaccount2:")
Bankaccount2.close_account()

