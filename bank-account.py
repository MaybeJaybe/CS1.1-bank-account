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
        amount = float(amount)
        self.balance += amount
        print(f"Amount Deposited: ${amount}")
        print(" ")

    def withdraw(self, amount):
        # take parameter amount, subtract amount from balance
        amount = float(amount)
        self.balance -= amount
        if self.balance >= 0:
            print(f"Amount Withdrawn: ${amount}")
            print(" ")
        else:
            # if user withdraws more than current balance charge overdraft fee of $10
            self.balance -= 10
            print("Insufficient funds. An overdraft fee of $10.00 has been charged to your account.")
            print(" ")

    def get_balance(self):
        self.rounded = str(round(self.balance, 2))
        print("Thank you for using The Bank of Dad.")
        print(f"Your balance is ${self.rounded}. You should get a decent job like your cousin.")
        print(" ")
        return self.balance

    def add_interest(self):
        # add interest to the users balance, interest rate is 1%, or 0.083% per month
        interest = self.balance * 0.00083
        self.interest = interest
        self.balance += self.interest
        return self.balance

    def print_reciept(self):
        self.rounded = str(round(self.balance, 2))
        print(" ")
        print("Account Summary:")
        print(" ")
        print("Name:", self.full_name)
        print("Routing Number:", self.routing_number)
        print("Account Number:", self.account_number)
        print(f"Balance: ${self.rounded}")
        print(" ")

# atm screens
def login_screen(account_list):
    print("Welcome to The Bank of Dad ATM")
    name = input("Enter your name to log in or press 0 to exit: ")
    if name == "0":
        return -1
    for i in range(len(account_list)):
        if name == account_list[i].full_name:
            return i
    return None

def atm_menu():
    print("Menu")
    print("Press 1 to make a deposit")
    print("Press 2 to make a withdrawl")
    print("Press 3 to check your balance")
    print("Press 4 for account summary")
    print("Press 5 to log out")
    print("Press 0 to exit")
    return input("Make your selection: ")


# outside class, define 3 different bank acct examples using BankAccount object
if __name__ == "__main__":
    # this clears console log
    print(chr(27) + "[2J")

    account_list = []
    account_list.append(BankAccount("Jay MayMay"))
    account_list.append(BankAccount("Ares Allan"))
    account_list.append(BankAccount("Lexi Lou-Ann"))

    profile = None

    while True:
        if not profile:
            profile = login_screen(account_list)
            if not profile:
                print("That is not the name of my child, try again.")
                print(" ")
            if profile == -1:
                break

        if profile:
            selection = atm_menu()
            if selection == "1":
                deposit_amount = input("How much do you want to deposit? ")
                account_list[profile].deposit(deposit_amount)
            elif selection == "2":
                withdraw_amount = input("How much would you like to withdraw? ")
                account_list[profile].withdraw(withdraw_amount)
            elif selection == "3":
                account_list[profile].get_balance()
            elif selection == "4":
                account_list[profile].print_reciept()
            elif selection == "5":
                profile = None
            elif selection == "exit" or selection == "0":
                break
            else:
                print("Error. Dad does not compute. Try again.")
                print(" ")