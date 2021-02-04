class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        # randomly generated 8 digit number unique per acct
        self.account_number = account_number
        # 9 digit number, same for all accts
        self.routing_number = routing_number
        # should start at 0
        self.balance = balance

    # methods deposit, withdraw, get_balance, add_interest, print_reciept
    def deposit(self, amount):
        # take parameter amount, add amount to the balance
        print("Amount Deposited: $")

    def withdraw(self, amount):
        # take parameter amount, subtract amount from balance
        print("Amount Withdrawn: $")
        # if user withdraws more than current balance,
        print("Insufficient funds.")
        # also, charge overdraft fee of $10.

    def get_balance(self):
        print("user friendly message with acct balance")
        # return(balance)


    def add_interest(self):
        # add interest to the users balance, interest rate is 1%, or 0.083% per month
        # interest = balance * 0.00083
        print("interest amount")

    def print_reciept(self):
        print("looks like this:")
        # Joi Anderson
        # Account No.: ****5678
        # Routing No.: 98765432
        # Balance: $100.00 

# outside class, define 3 different bank acct examples using BankAccount object
