# By default, python does not provide abstract classes. Python comes with a module that provides the
# base for defining Abstract Base Class (ABC) and that module name is ABC. ABC works by decorating
# methods of the base class as an abstract and then registering concrete classes as implementations
# of the abstract base. A method becomes abstract when decorated with the kewword @abstractmethod.

from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("Triangle have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("Pentagon have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("Hexagon have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("Quadrilaterals have 4 sides")


# Driver code
R = Triangle()
R.no_of_sides()

K = Quadrilateral()
K.no_of_sides()

R = Pentagon()
R.no_of_sides()

K = Hexagon()
K.no_of_sides()
