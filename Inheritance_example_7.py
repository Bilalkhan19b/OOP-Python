class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        super().buy()


s = SmartPhone(25000, "Samsung", 12)
s.buy()
