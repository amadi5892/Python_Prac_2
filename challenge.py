# For this challenge, create a bank account class that has two attributes
#   owner, balance
# And two methods:
#   deposit,withdraw

class Account():

    def __init__(self,owner,balance):

        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return (f'Account owner: {self.owner}\nAccount balance: ${self.balance}')

    def deposit(self,amount):

        self.balance = self.balance + amount
        return 'Deposit Accepted'

    def withdraw(self,amount):

        if amount > self.balance:
            return 'Funds Unavailable!'
        else:
            self.balance = self.balance - amount
            return 'Withdraw Accepted'

acct1 = Account('Parrish Williamson',100)

print(acct1)
print(acct1.owner)
print(acct1.balance)
print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1.withdraw(500))