#!/usr/bin/python3

class square():
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        return (self.width * 4)

    def __str__(self):
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
