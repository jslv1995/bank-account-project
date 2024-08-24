import pytest
from main import Bank, CheckingAccount, SavingsAccount

## Test Bank: Parent Class
def test_get_bank_account_owners_name():
    account = Bank("frankie knuckles")
    result = account.get_account_owner()
    assert result == "Frankie Knuckles"

def test_get_bank_account_number():
    Bank.account_number = 1 # Reset to ensure consistent test results.
    account = Bank("frankie knuckles")
    result = account.get_account_number()
    assert result == 2

def test_get_checking_balance():
    account = CheckingAccount("frankie knuckles", 100)
    result = account.get_balance()
    assert account.balance == 100
    assert result == "Current balance: $100.00."

def test_get_savings_balance():
    account = SavingsAccount("frankie knuckles", 100)
    result = account.get_balance()
    assert account.balance == 100
    assert result == "Current balance: $100.00."

# Tests deposit and the update to transaction history.
def test_deposit():
    account = CheckingAccount("frankie knuckles", 100)
    result = account.deposit(50)
    assert account.balance == 150
    assert result == "Thank you for your deposit. Your updated balance is $150.00."
    assert account.transaction_history[-1] == "Deposit: 50"

def test_negative_deposit():
    account = CheckingAccount("frankie knuckles", 100)
    result = account.deposit(-25)
    assert account.balance == 100
    assert result == "Error: Unable to deposit negative amount."

# Test withdrawal and the update to transaction history.
def test_negative_withdrawal():
    account = CheckingAccount("frankie knuckles", 100)
    result = account.withdraw(-50)
    assert account.balance == 100
    assert result == "Error: Withdrawal amount must be greater than $0.00"

def test_withdrawal():
    account = CheckingAccount("frankie knuckles", 100)
    result = account.withdraw(50)
    assert account.balance == 50
    assert result == "Please take your cash. Your updated balance is $50.00."
    assert account.transaction_history[-1] == "Withdrawal: -50"

def test_exceeding_withdrawal():
    account = CheckingAccount("frankie knuckles", 100)
    result = account.withdraw(500)
    assert account.balance == 100
    assert result == "Error: Insufficient funds."

## Test Savings Account.

# Tests interest payment amount, updated account balance, and updated transaction history.
def test_interest_payment():
    account = SavingsAccount("frankie knuckles", 100)
    result = account.pay_monthly_interest()
    expected_interest = round(100 * (0.05/12) ,2) # $100 balance, times monthly interest payment at 5% APY
    assert account.balance == 100 + expected_interest
    assert result == f"You've earned ${expected_interest} in interest this month!"
    assert account.transaction_history[-1] == f"Interest paid: ${expected_interest}"

