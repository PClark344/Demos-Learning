class Shape:
    def __init__(self,shape_type):
        self.__shape_type = shape_type

def get_type(self):
    return self.__shape_type

def get_area(self):
    pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

class Triangle(Shape):
    def __init__(self,base,height):
        self.__base = base
        self.__height = height

    def get_area(self):
        return 0.5 * self.__width * self.__height

