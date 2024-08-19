
class BankAccount():
    """A bank account that tracks user's available balances and transfers."""

    def __init__(self, account_owner, balance=0, account_type='checking'):
        """Initialize the attributes of a bank account."""
        self.account_owner = account_owner
        self.balance = balance
        self.account_type = account_type
        self.transaction_history = []

    def get_account_owner(self):
        """Return the account owner's name."""
        return self.account_owner.title()

    def get_balance(self):
        """Check current balance."""
        return f"Current balance: ${self.balance:.2f}."
        
    def get_transaction_history(self):
        """Return the list of transactions."""
        return f"Settled transactions: {self.transaction_history}"

    def deposit(self, requested_deposit_amount):
        """Deposit a cash amount, must be positive."""
        try:
            if requested_deposit_amount >= 0:
                self.balance += requested_deposit_amount
                self.transaction_history.append(f"Deposit: {requested_deposit_amount}")
                return f"Thank you for your deposit. Your updated balance is ${self.balance:.2f}."
            else:
                return "Error: Unable to deposit negative amount."
            
        except (TypeError, ValueError):
            return "Please enter a valid number."        
    
    def withdraw(self, requested_withdrawal_amount):
        """Withdraw a cash amount, no more than current balance."""
        try:
            if requested_withdrawal_amount <= self.balance:
                self.balance -= requested_withdrawal_amount
                self.transaction_history.append(f"Withdrawal: {requested_withdrawal_amount * -1}")
                return f"Please take your cash. Your updated balance is ${self.balance:.2f}."
            else:
                return "Error: Insufficient funds."
            
        except (TypeError, ValueError):
            return "Please enter a valid number"
        
class SavingsAccount(BankAccount):
    """Allows the owner to earn interest."""

    def __init__(self, account_owner, balance=0, account_type='savings'):
        """Initialize the savings account with 5% APY."""
        # Inherit the Bank Account attributes.
        super().__init__(account_owner, balance, account_type)
        transaction_history = []
        self.interest_rate = 0.05

    def pay_monthly_interest(self):
        """Credit the account monthly interest."""

        # Calculate monthly rate and amount.
        monthly_interest_rate = float(self.interest_rate/12)
        monthly_interest_paid = round(self.balance * monthly_interest_rate,2)

        # Credit the monthly amount of interest.
        self.balance += monthly_interest_paid
        self.transaction_history.append(f"Interest paid: ${monthly_interest_paid}")
        return f"You've earned ${monthly_interest_paid} in interest this month!"
