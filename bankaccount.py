class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def __sub__(self, other):
        if isinstance(other, BankAccount):
            new_balance = self