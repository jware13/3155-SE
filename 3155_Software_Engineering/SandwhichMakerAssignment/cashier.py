class Cashier:
    def __init__(self, name):
        self.name = name

    def process_coins(self):
        """Return the total calculated from coins inserted."""
        coin_values = {
            "quarters": 0.25,
            "dimes": 0.10,
            "nickels": 0.05,
            "pennies": 0.01
        }
        total = 0
        for coin, value in coin_values.items():
            count = int(input(f"How many {coin}?: "))
            total += count * value
        return round(total, 2)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry that is not enough money. Money refunded.")
            return False
        change = round(coins - cost, 2)
        print(f"Here is your change: ${change:.2f}")
        return True