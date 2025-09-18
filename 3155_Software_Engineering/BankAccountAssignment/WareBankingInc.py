class WareBankAccount:
    bankName: str = "WareBankingInc"

    def __init__(self, customer_name: str, account_number:str, routing_number: str, current_balance: float, minimum_balance: float):
        # add the self and initialize the variables above
        self.customer_name = customer_name
        self.current_balance = float(current_balance)
        self.minimum_balance = float(minimum_balance)
        self._account_number = account_number
        self._routing_number = routing_number

    # deposit method
    def deposit(self, amount: float):
        if amount > 0:
            self.current_balance += amount
            print(f"[{self.customer_name}] Deposited ${amount:.2f}. So your new balance is ${self.current_balance:.2f}")
        else:
            print("You must deposit a positive amount of money")

    # withdraw method

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.current_balance:
            self.current_balance -= amount
            print(f"[{self.customer_name}] Withdrew ${amount:.2f}. So your new balance is ${self.current_balance:.2f}")
            return True
        elif amount <= 0:
            print("You must withdraw a positive amount of money.")
        else:
            print("Insufficient Funds")

    # transfer method
    def transfer(self, other: "WareBankAccount", amount: float) -> bool:
        if self.withdraw(amount):
            other.deposit(amount)
            print(f"[{self.customer_name}] Transferred ${amount:.2f} to [{other.customer_name}]")
            return True
        else:
            print("Transfer failed due to insufficient funds.")
            return False

    # print_customer_information (including bank title)

    def print_customer_information(self):
        print(f"Bank: {self.bankName}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self._routing_number}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
        print("-" * 30)


# Creating two instances to make sure it works

if __name__ == '__main__':
    james = WareBankingInc("James Harden", current_balance=50000000, minimum_balance=1000000)
    tracy = WareBankingInc("Tracy McGrady", current_balance=35000000, minimum_balance=750000)

    james.print_customer_information()
    tracy.print_customer_information()

    james.deposit(1000000)
    tracy.withdraw(1000000)
