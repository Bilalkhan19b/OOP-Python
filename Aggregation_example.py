class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pincode, new_district):
        self.name = new_name
        self.address.change_address(new_city, new_pincode, new_district)


class Address:
    def __init__(self, city, pincode, district):
        self.city = city
        self.pincode = pincode
        self.district = district

    def change_address(self, new_city, new_pincode, new_district):
        self.city = new_city
        self.pincode = new_pincode
        self.district = new_district


add = Address("Karachi", "700561", "Central")
cust = Customer("Bilal", "Male", add)

cust.edit_profile("Asad", "Lahore", "11111", "East")

print(cust.name)
print(cust.gender)
print(cust.address.city)
print(cust.address.pincode)
print(cust.address.district)
