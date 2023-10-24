from cardHolder import CardHolder


def print_menu():
    print(f"{current_customer.get_firstname()} Welcome to main menu")
    print("Please choose from one of the following options ...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")


def deposit(CardHolder):
    try:
        deposit = float(input("How much $$ would you like to deposit: "))
        CardHolder.set_balance(CardHolder.get_balance() + deposit)
        print(f"Thank you for your $$. Your new balance is: {str(CardHolder.get_balance())}")

    except:
        print("Invalid input")


def withdraw(CardHolder):
    try:
        withdraw = float(input("How much $$ would you like to withdraw: "))

        if withdraw < CardHolder.get_balance():
            CardHolder.set_balance(CardHolder.get_balance() - withdraw)
            print("Withdraw money successfully")
        else:
            print("Insufficient money on your account")
    except:
        print("Invalid input")


def check_balance(CardHolder):
    print(f"Your current balance is : {CardHolder.get_balance()}")


def exit():
    print("you have already exit your account")


if __name__ == "__main__":

    list_of_customers = []
    list_of_customers.append(CardHolder("3456789088893033", 1134, "John", "Grif", 200))
    list_of_customers.append(CardHolder("3456789088878889", 2234, "Dawn", "smift", 200))
    list_of_customers.append(CardHolder("3456789088444889", 3634, "eric", "liu", 200))
    # input customer for pin
    while True:
        try:
            customer_pin = int(input("Please enter your pin：").strip())

            customer = [user for user in list_of_customers if user.get_pin() == customer_pin]
            if (len(customer) > 0):
                current_customer = customer[0]
                break;
            else:
                print("Invalid pin, Please try again")

        except:
            print("Invalid PIN. Please try again")

    while True:
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input, Please try again")
        if (option == 1):
            deposit(current_customer)
        elif (option == 2):
            withdraw(current_customer)
        elif (option == 3):
            check_balance(current_customer)
        elif (option == 4):
            exit()
            break;

    # while true:
    #     try:
    #         customerPin = int(input("Please enter your pin: ").strip())
    #         if()
    #     except:
    #         print("Invalid Pin, Please try again")
