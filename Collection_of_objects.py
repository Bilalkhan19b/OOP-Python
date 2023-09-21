class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am", self.name, "and I am", self.age)


c1 = Customer("Bilal", 22)
c2 = Customer("Asad", 19)
c3 = Customer("Khan", 34)

L = [c1, c2, c3]
for i in L:
    print(i.name, i.age)
    i.intro()
