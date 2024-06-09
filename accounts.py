
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance"""
    def __init__(self, name, balance):
        """Initialize an account object"""
        # if balance is < 0 exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= 0.00.')
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money to the account"""
        if amount <= Decimal('0.00'):
            raise ValueError('Amount must be > 0.00')
        self.balance += amount    

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > self.balance:
            raise ValueError('Amount must be <= balance')
        elif amount <= Decimal('0.00'):
            raise ValueError('Amount must be positive')
        self.balance -= amount
