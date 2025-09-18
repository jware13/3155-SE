from WareBankingInc import WareBankAccount

class CheckingAccount(WareBankAccount):
    def __init__(self, customer_name: str, account_number: str, routing_number: str, per_transfer_limit: float, current_balance: float = 0.0, minimum_balance: float = 0.0):
        super().__init__(customer_name, account_number, routing_number, current_balance, minimum_balance)
        self.per_transfer_limit = per_transfer_limit

    def transfer(self, other: "WareBankAccount", amount: float) -> bool:
        if amount > self.per_transfer_limit:
            print(f"Transfer amount exceeds the per-transfer limit of ${self.per_transfer_limit:.2f}.")
            return False
        return super().transfer(other, amount)