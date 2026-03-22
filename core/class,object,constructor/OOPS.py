# 1. Design a banking system with:
# • An abstract base class Account with deposit(), withdraw(),
# calculate_interest().
# • Subclasses: SavingsAccount, CurrentAccount, FixedDepositAccount.
# • Each account must:
# o Encapsulate balance (private)
# o Provide controlled access through properties
# o Override interest calculation differently
# • Include a static method to validate amount.
# • Include a class method to update bank-wide interest policies.
# Demonstrate:
# • Polymorphic behavior by iterating through all account types
# • Preventing direct access to balance
# • Multiple interest strategies
from abc import ABC,abstractmethod
class Account:
    @abstractmethod
    def deposit(self):
        print("deposited")
    @abstractmethod
    def withdraw(self):
        print("withdrawn")
class savings_account(Account):
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self):
        print("savings deposit")
    def withdraw(self):
        print("savings withdrawn")
class current_account(Account):
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self):
        print("current deposit")
    def withdraw(self):
        print("current withdrawn")
#####
from abc import ABC, abstractmethod
class Account(ABC):
    bank_interest_rate = 5
    def __init__(self, balance):
        self.__balance = balance
    # property for controlled access
    @property
    def balance(self):
        return self.__balance
    # deposit method
    def deposit(self, amount):
        if Account.validate_amount(amount):
            self.__balance += amount
    # withdraw method
    def withdraw(self, amount):
        if Account.validate_amount(amount) and amount <= self.__balance:
            self.__balance -= amount
    # abstract method
    @abstractmethod
    def calculate_interest(self):
        pass
    # static method
    @staticmethod
    def validate_amount(amount):
        return amount > 0
    # class method
    @classmethod
    def update_interest_policy(cls, new_rate):
        cls.bank_interest_rate = new_rate
# Savings Account
class SavingsAccount(Account):

    def calculate_interest(self):
        return self.balance * 0.04
# Current Account
class CurrentAccount(Account):
    def calculate_interest(self):
        return 0   # usually no interest
# Fixed Deposit Account
class FixedDepositAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.07
# Creating objects
accounts = [SavingsAccount(10000),SavingsAccount(10000),FixedDepositAccount(50000)]
# Polymorphism
for acc in accounts:
    print(type(acc).__name__)
    print("Balance:", acc.balance)
    print("Interest:", acc.calculate_interest())
    print()
