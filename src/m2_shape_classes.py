import math

###############################################################################
# TODO: 1.
#
#   For this _todo_, create a parent class called Shape. It should have an
#   __init__() function that sets two properties:
#       - width     <- int
#       - height    <- int
#
#   It should have two methods:
#       - area
#       - perimeter
#
#   These methods should return their respective calculation. This Shape class
#   should assume that the shape is a rectangle, so these calculations are as
#   follows.
#
#       area = width * height
#
#       perimeter = (width * 2) + (height *2)
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
    
class Shape():
    def __init__(self, width, height):
        self.width = width 
        self.height = height 

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)


###############################################################################
# TODO: 2.
#
#   For this _todo_, create a child class called Rectangle that inherits its
#   class from Shape. Since Shape already assumes the shape is a rectangle, we
#   don't really need to modify anything. Remember that you can create an empty
#   class by using the pass keyword.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

class Rectangle(Shape):
    pass 

###############################################################################
# TODO: 2.
#
#   For this _todo_, create a child class called Circle that inherits its class
#   from Shape.
#
#   Now, a circle is a little bit different because it doesn't really have a
#   height and width. It simply has a radius. So, it's __init__() method should
#   only set a radius parameter (and not width and height).
#
#   The calculations for a circle are different two, so these methods should
#   use these calculations.
#
#       area = Pi * (radius ** 2)
#
#       perimeter = 2 * Pi * radius     <-- this is also called circumference
#
#   I have imported the math module at the top of this file, so you can use
#   math.pi to get the value of Pi.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

class Circle(Shape): 
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius


###############################################################################
# TODO: 3.
#
#   For this _todo_, create a child class called Diamond that inherits its
#   class from Shape. A Diamond does have a height and width so you don't need
#   to overrite the __init__() function.
#
#   The calculations you will need are:
#
#       area = (width * height) / 2
#
#       perimeter = 2 * sqrt(width ** 2 + height ** 2)
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 4.
#
#   For this _todo_, create three different objects and save each to a
#   variable. Create a Rectangle, Circle, and Diamond.
#
#   You should also print each one's area and perimeter using the object's
#   methods.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
