class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class Smartphone(Phone):
    pass

class FeaturePhone(Phone):
    pass

s=Smartphone(25000,"Apple","12px")
f=FeaturePhone(1000,"Samsung","48px")

s.buy()
f.buy()