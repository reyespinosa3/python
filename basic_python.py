# Creating Banking classes
class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if (amount < 0):
            print('Please enter a new amount')
        elif (amount == 0):
            print('No deposit will be made at this time')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if (amount < 0):
            print('No withdrawls made at this time')
        elif (amount > self.balance):
            print('You can NOT take out more than you have in your account!')
        else:
            self.balance -= amount

    def accumulate_interest(self):
        self.balance = self.balance + (self.balance * .02)

basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

class ChildrensAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if (amount < 0):
            print('Please enter a new amount')
        elif (amount == 0):
            print('No deposit will be made at this time')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if (amount < 0):
            print('No withdrawls made at this time')
        elif (amount > self.balance):
            print('You can NOT take out more than you have in your account!')
        else:
            self.balance -= amount
    def accumulate_interest(self):
        self.balance = self.balance + (self.balance * .00)


childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

class OverdraftAccount(BankAccount):
    def __init__(self):
        self.balance = 0
        self.overdraft_penalty = 40

    def deposit(self, amount):
        if (amount < 0):
            print('Please enter a new amount')
        elif (amount == 0):
            print('No deposit will be made at this time')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if (amount < 0):
            print('No withdrawls made at this time')
        else:
            (amount > self.balance)
            print('You can NOT take out more than you have in your account!')
            self.balance -= self.overdraft_penalty

    def accumulate_interest(self):
        if (self.balance <= 0):
            print('No interest is accumulating')
        else:
            self.balance = self.balance + (self.balance * .00)

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))

# savings = Bankaccount('savings')
# checking = Bankaccount('checking')
#
# print('My {} account has ${}'.format(savings.kind, savings.balance))
# print('My {} account has ${}'.format(checking.kind, checking.balance))
#
# print('How much do you want to deposit into checking?')
# amount = input()
# checking.deposit(int(amount))
# print('My {} account now has ${}'.format(checking.kind, checking.balance))
#
#
# print('How much do you want to deposit into savings?')
# amount = input()
# savings.deposit(int(amount))
# print('My {} account now has ${}'.format(savings.kind, savings.balance))
#
# print('How much do you want to withdrawl from checking?')
# amount = input()
# checking.withdrawl(int(amount))
# print('Your {} account now has ${}'.format(checking.kind, checking.balance))
#
# print('How much do you want to withdrawl from savings?')
# amount = input()
# savings.withdrawl(int(amount))
# print('Your {} account now has ${}'.format(savings.kind, savings.balance))
#
# print('My {} account has ${}'.format(savings.kind, savings.balance))
# print('My {} account has ${}'.format(checking.kind, checking.balance))
