import threading


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False
        self._lock = threading.Lock()

    def get_balance(self):
        if self.is_open:
            return self.balance
        else:
            raise ValueError("Cannot check balance of a closed account")

    def open(self):
        if not self.is_open:
            self.is_open = True
            self.balance = 0
        else:
            raise ValueError("Bank account is already open!")

    def deposit(self, amount):
        with self._lock:
            if self.is_open:
                if amount >= 0:
                    self.balance += amount
                else:
                    raise ValueError("Deposit amount must be greater than 0")
            else:
                raise ValueError("Account must be open before performing changes")

    def withdraw(self, amount):
        with self._lock:
            if self.is_open:
                if amount >= 0:
                    if amount <= self.balance:
                        self.balance -= amount
                    else:
                        raise ValueError("You do not have enough money to withdraw that amount!")
                else:
                    raise ValueError("Withdraw amount must be greater than 0")
            else:
                raise ValueError("Account must be open before performing changes")

    def close(self):
        if self.is_open:
            self.is_open = False
        else:
            raise ValueError("Bank account is already closed!")
