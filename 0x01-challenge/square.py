#!/usr/bin/python3

class square():
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Calculate perimeter of the square """
        return 2 * (self.width + self.height)

    def __str__(self):
        """ String representation of the square """
        return "Square(width={}, height={})".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
