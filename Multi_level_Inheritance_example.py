class Product:
    def review(self):
        print("Product customer review")
class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class Smartphone(Phone):
    pass


s=Smartphone(25000,"Apple","12px")
p=Phone(1000,"Samsung","48px")

s.buy()
s.review()
p.review()