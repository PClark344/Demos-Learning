import abc

# abstract classes
class Toy(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def show(self):
        pass

class color(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def show_color(self):
        pass

# concrete classes
class Car(Toy):
    def show(self):
        print('Remote Ctrl Car')

class AFig(Toy):
   def show(self):
        print('Action Man')

class Cons(Toy):
   def show(self):
        print('Meccano')

import abc

# abstract classes
class Toy(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def show(self):
        pass

class Color(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def show_color(self):
        pass

# concrete classes
class Car(Toy):
    def show(self):
        print('Remote Ctrl Car')

class ActionFigure(Toy):
   def show(self):
        print('Action Man')

class ConstructionToy(Toy):
   def show(self):
        print('Mecanno')

class Red(Color):
    def show_color(self):
        print('Red')

class Blue(Color):
    def show_color(self):
        print('Blue')

class Green(Color):
    def show_color(self):
        print('Green')

# Abstract Factory Classes

class AbstractFactory(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def get_color(self):
        pass

    @abc.abstractmethod
    def get_toy(self):
        pass

class ColorfulToysFactory(AbstractFactory):
    def get_toy(self,toy_type):
        if toy_type == None:
            return None

        if toy_type == 'car'
            return Car()
        elif toy_type == 'action figure':
            return ActionFigure()
        elif toy_type == 'construction toy':
            return ConstructionToy()

        return None

    def get_color(self,color_type):
        if color_type == None:
            return None

        if color_type == 'red'
            return Red()
        elif toy_type == 'blue':
            return Blue()
        elif toy_type == 'green':
            return Green()
           
        return None

