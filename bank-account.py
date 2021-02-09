import secrets
# secrets is a more secure random number library, makes numbers less predictable
import string
# banks apparently use acct numbers in a string

# The Bank of Dad
class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name
        # randomly generated 8 digit number unique per acct
        self.account_number = ''.join(secrets.choice(string.digits)for i in range(8))
        # 9 digit number, same for all accts
        self.routing_number = 226576883
        # should start at 0
        self.balance = float(0)

    # methods def
    def deposit(self, amount):
        # take parameter amount, add amount to the balance
        self.balance += amount
        total = float(amount)

        print(f"Amount Deposited: ${total}")
        print(f"New Balance: ${self.balance}")

    def withdraw(self, amount):
        # take parameter amount, subtract amount from balance
        if self.balance >= amount:
            self.balance -= amount
            total = float(amount)
            print(f"Amount Withdrawn: ${total}")
            print(f"New Balance: ${self.balance}")
        else:
            self.balance -= amount
            # if user withdraws more than current balance charge overdraft fee of $10
            self.balance -= 10
            print("Insufficient funds. An overdraft fee of $10.00 has been charged to your account.")
            print(f"New Balance: ${self.balance}")

    def get_balance(self):
        print("Thank you for using The Bank of Dad.")
        print(f"Your balance is ${self.balance}. You should get a job like your sister.")
        return self.balance


    # def add_interest(self, interest, balance):
        # add interest to the users balance, interest rate is 1%, or 0.083% per month
        # interest = balance * 0.00083
        # self.interest = interest
        # self.balance += self.interest
        # print("interest amount")

    def print_reciept(self):
        print("Account Summary:")
        print(" ")
        print("Name: ", self.full_name)
        print("Routing Number:", self.routing_number)
        print("Account Number:", self.account_number)
        print("Balance: $", self.balance)

# outside class, define 3 different bank acct examples using BankAccount object

jay = BankAccount("Jay MayMay")
ares = BankAccount("Ares Allan")
lexi = BankAccount("Lexi Lou-Ann")

print(jay.full_name)
print(f"Account Number: {str(jay.account_number)}")
print(f"Routing Number: {jay.routing_number}")

print(ares.full_name)
print(f"Account Number: {str(ares.account_number)}")
print(f"Routing Number: {ares.routing_number}")

print(lexi.full_name)
print(f"Account Number: {str(lexi.account_number)}")
print(f"Routing Number: {lexi.routing_number}")


jay.deposit(10)
jay.withdraw(10)
ares.deposit(100)
jay.withdraw(10)
ares.withdraw(45)
jay.get_balance()
ares.get_balance()
jay.print_reciept()
ares.print_reciept()
lexi.print_reciept()


# account_list = [jay, ares, lexi]

# for account in account_list:
#     account.account_number()