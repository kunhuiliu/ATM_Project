class CardHolder:
    def __init__(self, cardnum, pin, firstname, lastname, balance):
        self.cardnum = cardnum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def get_cardnum(self):
        return self.cardnum

    def get_pin(self):
        return self.pin

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_balance(self):
        return self.balance

    # reassign values for users
    def set_cardnum(self, newVal):
        self.cardnum = newVal

    def set_pin(self, newVal):
        self.pin = newVal

    def set_firstname(self, newVal):
        self.firstname = newVal

    def set_lastname(self, newVal):
        self.firstname = newVal

    def set_balance(self, newVal):
        self.balance = newVal

    def print_out(self):
        print(f"Card #: {self.cardnum}")
        print(f"Pin: {self.pin}")
        print(f"First Name: {self.firstname}")
        print(f"Last Name: {self.lastname}")
        print(f"Balance: {self.balance}")
