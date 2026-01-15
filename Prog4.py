class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")
    
    def check_balance(self):
        print("Balance : ", self.balance)

account = BankAccount("User")
while True:
    print("\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit")
    ch = input("Enter amount: ")
    
    if ch == '1':
        amt = int(input("Enter amount: "))
        account.deposit(amt)
    elif ch == '1':
        amt = int(input("Enter amount: "))
        account.withdraw(amt)
    elif ch == '3':
        account.check_balance()
    elif ch == '4':
        break
    else:
        print("Invalid Account")