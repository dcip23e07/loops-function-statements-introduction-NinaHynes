class ATM:
    def __init__(self, customer_balance, min_withdrawal_amount, max_withdrawal_amount):
        self.customer_balance = customer_balance
        self.min_withdrawal_amount = min_withdrawal_amount
        self.max_withdrawal_amount = max_withdrawal_amount

    def withdraw_cash(self, amount):
        if amount < self.min_withdrawal_amount or amount > self.max_withdrawal_amount:
            raise ValueError("Withdrawal amount is out of range")

        if amount > self.customer_balance:
            raise ValueError("Insufficient balance")

        self.customer_balance -= amount
        return amount

def main():
    atm = ATM(100000, 10, 5000)

    print("Welcome to the ATM!")

    while True:
        want_to_withdraw = input("Withdraw money? (y/n): ")
        #function withdraw money

        if want_to_withdraw == "n":
            break

        withdrawal_amount = float(input("Enter the amount you want to withdraw: "))

        try:
            atm.withdraw_cash(withdrawal_amount)
        except ValueError as e:
            print(e)
        else:
            print("Cash dispensed successfully!")
            print("Remaining balance:", atm.customer_balance)

    print("Thank you for using the ATM!")


if __name__ == "__main__":
    main()