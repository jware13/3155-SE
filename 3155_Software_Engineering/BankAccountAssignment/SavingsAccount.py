from WareBankingInc import WareBankAccount

class SavingsAccount(WareBankAccount):
    def __init__(self, customer_name: str, account_number: str, routing_number: str, interest_rate: float, current_balance: float = 0.0, minimum_balance: float = 0.0):
        super().__init__(customer_name, account_number, routing_number, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def apply_interest(self): 
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print(f"[{self.customer_name}] Applied interest of ${interest:.2f}. New balance is ${self.current_balance:.2f}")
        