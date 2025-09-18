from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

def main():
    print("Welcome to Ware Banking Inc.")
    # create at least two instances of each class
    savings1 = SavingsAccount("James Harden", "SA123", "RT001", interest_rate=0.03, current_balance=1000, minimum_balance=100)
    savings2 = SavingsAccount("Tracy McGrady", "SA456", "RT002", interest_rate=0.04, current_balance=2000, minimum_balance=200)

    checking1 = CheckingAccount("TyTy Washington", "CA123", "RT003", per_transfer_limit=500, current_balance=1500, minimum_balance=150)
    checking2 = CheckingAccount("Alperen Sengun", "CA456", "RT004", per_transfer_limit=1000, current_balance=2500, minimum_balance=250)

    # demonstrate the functionality of each method in each class
    savings1.print_customer_information()
    savings2.print_customer_information()
    checking1.print_customer_information()
    checking2.print_customer_information()
    print()
    savings1.deposit(500)
    savings2.withdraw(300)
    checking1.transfer(checking2, 400)
    checking2.transfer(savings1, 200)
    savings1.apply_interest()
    savings1.print_customer_information()
    savings2.print_customer_information()
    checking1.print_customer_information()
    checking2.print_customer_information()
    print()

if __name__ == "__main__":
    main()

    




