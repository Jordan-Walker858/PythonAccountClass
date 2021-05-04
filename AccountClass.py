# Account Class that includes an ID, Balance, and Annual interest rate for constructor parameters
# Includes methods to set and get ID, balance, withdraw, deposit, monthly and annual interest rate
class Account:
    def __init__(self, id = 0, balance = 0, annualIntRate = 0.0):
        self.__id = id
        self.__balance = balance
        self.__annualIntRate = annualIntRate
    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id
    def setBalance(self, balance):
        self.__balance = balance
    def getBalance(self):
        return self.__balance
    def withdraw(self, ammount):
        self.__balance -= ammount
    def deposit(self, ammount):
        self.__balance += ammount
    def setAnnIntRate(self, annualIntRate):
        self.__annualIntRate = annualIntRate
    def getAnnIntRate(self):
        return self.__annualIntRate / 100
    def getMonthlyInterestRate(self):
        return self.getAnnIntRate() / 12
    def getMonthlyInterest(self):
        return self.getMonthlyInterestRate() * self.getBalance()
# Problem asks to create 10 user accounts w/ $100 balance and 4.5% annual interest rate
# Create ATM function
def ATM():
    # create a list of accounts
    accountLst = []
    # for loop to create accounts with the i variable for the ID
    for i in range(10):
        accountLst.append(Account(i, 100, 4.5))
    # Create infinite loop for ATM
    while True:
        uid = int(input("Enter your ID: "))
        while uid < 0 or uid > 9: 
            uid = int(input("Invalid Input. Enter your ID: "))
        # create an instance of the class to perform methods
        accInstance = accountLst[uid]
        print("Main Menu\n", "1. check balance\n", "2. withdraw\n", "3. deposit\n", "4. exit")
        # Allow user to enter choice and perform methods pertaining to their accounts
        choice = int(input("Enter a choice: "))
        if choice == 1:
            print("The balance is", accInstance.getBalance())
        elif choice == 2:
            amt = eval(input("Enter an amount to withdraw: "))
            accInstance.withdraw(amt)
        elif choice == 3:
            dep = eval(input("Enter an amount to deposit: "))
            accInstance.deposit(dep)
        elif choice == 4:
            break
# Call ATM function
ATM()