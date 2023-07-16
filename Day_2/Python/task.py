####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.




class Account:
    def __init__(self,owner,deposite) -> None:
        self.owner = owner
        self.deposite = deposite
        self.balance = deposite
    def withdraw(self,withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.balance- self.withdraw_amount<0:
            return print(f"Your current balance is low ")
        self.balance = self.balance - self.withdraw_amount
        return self.withdraw_amount
    def deposit(self,deposite):
        self.deposite = deposite
        self.balance = self.balance + deposite
    def __repr__(self) -> str:
        return f'Owner:{self.owner},Deposite:{self.deposite}'
        
        
        
        


# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)




# 3. Show the account owner attribute
print(acct1.owner)




# 4. Show the account balance attribute
print(acct1.balance)




# 5. Make a series of deposits and withdrawals
acct1.deposit(50)




acct1.withdraw(75)




# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


print(acct1.balance)
# ## Good job!
