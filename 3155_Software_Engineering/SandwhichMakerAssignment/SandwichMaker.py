### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, needed in ingredients.items():
            if self.machine_resources.get(item, 0) < needed:
                print(f"Sorry there is not enough {item}")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        coin_values = {
            "large dollars": 1.00,
            "quarters": 0.25,
            "nickels": .05,
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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size} sandwich is ready!")


### Make an instance of SandwichMachine class and write the rest of the codes ###
def report_ingredients(res):
    print(f"Bread: {res['bread']} slice(s)")
    print(f"Ham: {res['ham']} slice(s)")
    print(f"Cheese: {res['cheese']} pound(s)")


def main():
    machine = SandwichMachine(resources)

    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()

        if choice == "off":
            break
        elif choice == "report":
            report_ingredients(machine.machine_resources)
        elif choice in recipes:
            order = recipes[choice]
            ingredients = order["ingredients"]
            cost = order["cost"]

            if not machine.check_resources(ingredients):
                continue
            coins = machine.process_coins()

            if not machine.transaction_result(coins, cost):
                continue
            machine.make_sandwich(choice, ingredients)
        else:
            print("Invalid option. Please choose one of the available choices.")
if __name__ == "__main__":
    main()