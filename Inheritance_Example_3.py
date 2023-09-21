class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera


class SmartPhone(Phone):
    pass


s = SmartPhone(25000, "Samsung", 12)
# The object of child class can not access the hidden members of the parent class.
print(s.__brand)
