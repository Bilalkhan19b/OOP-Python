class Atm:
    # static/Class Variable (same for all instances)
    __counter = 0

    # Special/Magic/Dunder Methods eg:(__str__,__init__,__add__)...etc
    def __init__(self):  # Constructor
        # Instance Variables (different for all instances)
        self.__pin = ""
        self.__balance = 0
        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter + 1

        self.__menu()

    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Not Allowed")

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin changed successfully")
        else:
            print("Not Allowed")

    def __menu(self):
        user_input = input("""
        Hello, How would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Bye")

    def create_pin(self):
        new_pin = input("Enter a new pin")
        self.__pin = new_pin
        print("Pin set successfully")

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount to deposit"))
            self.__balance = self.__balance + amount
            print("Deposit Successfully")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount to withdraw"))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("Withdraw Successful")
            else:
                print("You don't have enough balance")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid pin")
