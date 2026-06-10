class Student:
    def __init__(self,name,student_no,course):
        self.name=name
        self.student_no=student_no
        self.course=course

    def eats(self,food):
        print(f"{student1.name} eats {food}")

    def runs(self,how):
        print(f"{student1.name} runs {how}")

    def washes(self,unit):
        print(f"{student1.name} washes {unit}")

    def get_details(self):
        print("User details")
        print(f"Name:{self.name} -Student No:{self.student_no} -Course:{self.course}")
        print("-------------------")

# object 1
student1=Student("Emmanuel","s44","enginner")
print(type(student1))
print(student1)
student1.get_details()
student1.eats("doughnuts")
student1.runs("fast")
student1.washes("clothes")
# object 2
student2=Student("Mike","s50","law")
print(type(student2))
print(student2)
print(student2.name)
print(student2.student_no)
print(student2.course)
# object 3
student3=Student("David","s65","medicine")
print(type(student3))
print(student3)
print(student3.name)
print(student3.student_no)
print(student3.course)

class Bank_Account:
    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_number=account_number
        self.balance=balance
        self.owner_name=owner_name
        self.date_opened=date_opened

    def deposit(self):
           self.initial_amount=int(input("Enter amount to be deposited:"))
           return self.initial_amount

    def withdraw(self):
          self.final_amount=int(input("Enter amount to be withdrawn:"))
          return self.final_amount

    def check_balance(self):
          remaining_amount=(self.initial_amount-self.final_amount)+self.balance
          print(f"Available balance is:Ksh.{remaining_amount}")

    def display_info(self):
          remaining_amount=(self.initial_amount-self.final_amount)+self.balance
          print(f"{self.owner_name} available balance is Ksh.{remaining_amount}")

    def close_account(self):
          print(f"Thank you for choosing us,{self.owner_name}")
    def get_details(self):
        print("client details")
        print(f"Name:{self.owner_name} -Account Number:{self.account_number} -Balance:{self.balance} -Date Opened:{self.date_opened}")
        print("-------------------")
client=Bank_Account("09745453434",100,"Emmanuel Muteti","1-1-2026")
print(type(client))
print(client)
client.get_details()
client.deposit()
client.withdraw()
client.check_balance()
client.display_info()
client.close_account()