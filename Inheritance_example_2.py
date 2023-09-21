class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera


class SmartPhone(Phone):
    pass


s = SmartPhone(25000, "Samsung", 12)
print(s.brand)
