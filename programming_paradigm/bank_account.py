#!/bin/python3

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                print(f"${amount} withdrawn successfully.")
                return True
            else:
                print("Insufficient funds for the withdrawal.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        print(f"Current balance: ${self.__account_balance:.2f}")
