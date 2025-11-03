class BankAcct:
    def __init__(self, name, acct_num, amount=0.0, interest_rate=0.01):
        # create a new bank account with name, account name, account amount, and the interest rate
        self.name = name
        self.acct_num = acct_num
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)  # expressed as decimal (e.g., 0.05 = 5%)

    def deposit(self, amount):
        # adds money
        if amount > 0:
            self.amount += amount
            print(f"You have deposited ${amount:.2f}")
        else:
            print("Your deposit amount must be positive")

    def withdraw(self, amount):
        # withdraws money
        if 0 < amount <= self.amount:
            self.amount -= amount
            print(f"You have withdrawn ${amount:.2f}")
        elif amount > self.amount:
            print("Insufficient funds")
        else:
            print("Your withdrawal amount must be positive.")

    def adjust_interest_rate(self, new_rate):
        # alters account interest rate
        if new_rate >= 0:
            self.interest_rate = new_rate
            print(f"Interest rate is now adjusted to {new_rate * 100:.2f}%")
        else:
            print("Interest rate cannot be negative.")

    def calculate_interest(self, days):
        # calculates simple interest for a given number of days
        interest = self.amount * self.interest_rate * (days / 365)
        return interest

    def get_balance(self):
        # return the current balance
        return self.amount

    def __str__(self):
        # return a string representation of the account info
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.acct_num}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%")

# function to test with
def test_bank_account():
    # test account info
    acct = BankAcct("Ashleigh Ashodian", 123456, 5000.00, 0.05)
    print("Initial Account Info:")
    print(acct)
    print()

    # test deposit
    acct.deposit(600)
    print("Account after Deposit:")
    print(acct)
    print()

    # test withdraw
    acct.withdraw(400)
    print("Avccount after Withdrawal:")
    print(acct)
    print()

    # test adjusted interest rate
    acct.adjust_interest_rate(0.07)
    print("Account after interest rate adjustment:")
    print(acct)
    print()

    # test calculate interest for 30 days
    interest = acct.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")

    # test display of final balance
    print("\nFinal Account Summary:")
    print(acct)

# Run the test function
if __name__ == "__main__":
    test_bank_account()
