class Phone:
    def __init__(self,price,brand,camera):
        self.price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")


s=SmartPhone(25000,"Apple",12)

s.buy()