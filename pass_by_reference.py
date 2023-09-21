# class Customer:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
#
# def greet(customer):
#     if customer.gender=="male":
#         print("Hello",customer.name,"sir")
#     else:
#         print("Hello",customer.name,"ma'am")
#     cust2=Customer("Alexa","female")
#     return cust2
#
# cust=Customer("Bilal","male")
# new_cust=greet(cust)
# print(new_cust.name)


def change(L):
    print(id(L))
    L.append(5)
    print(id(L))


L1 = [1, 2, 3, 4]
print(id(L1))
print(L1)

# change(L1)

# By using pass by reference ,if you send mutable data types then the changes will happen in original,
# and if you send immutable data types like tuple then there will be no changes in original,
# Be careful when you are calling functions and sending mutable data types including objects of your class then
# there will be permanent changes by the functions,So you have to use cloning like below:
change(L1[:])

print(L1)
