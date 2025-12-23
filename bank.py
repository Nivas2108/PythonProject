class BankAccount:
    bank_name="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    @classmethod
    def change_bank(cls,new_account):
        cls.bank_name=new_account
    @staticmethod
    def validate_amount(x):
        return x>0
b1=BankAccount(holder="a",balance=10000)
b2=BankAccount(holder="b",balance=10000)
b3=BankAccount(holder="c",balance=10000)
b1.deposit(100)
b2.deposit(1000)
print(b1.balance)
print(b2.balance)
b1.change_bank("HDFC")
print(b1.bank_name)
print(b2.bank_name)
print(b3.bank_name)