import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

sandwich_maker = SandwichMaker(data.resources)
cashier = Cashier("Main Cashier")

### Make an instance of SandwichMaker class and write the rest of the codes ###
def report_ingredients(res):
    print(f"Bread: {res['bread']} slice(s)")
    print(f"Ham: {res['ham']} slice(s)")
    print(f"Cheese: {res['cheese']} pound(s)")

def main():


    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()

        if choice == "off":
            break
        elif choice == "report":
            report_ingredients(sandwich_maker.machine_resources)
        elif choice in data.recipes:
            order = data.recipes[choice]
            ingredients = order["ingredients"]
            cost = order["cost"]

            if not sandwich_maker.check_resources(ingredients):
                continue
            coins = cashier.process_coins()

            if not cashier.transaction_result(coins, cost):
                continue
            sandwich_maker.make_sandwich(choice, ingredients)
        else:
            print("Invalid option. Please choose one of the available choices.")
if __name__ == "__main__":
    main()