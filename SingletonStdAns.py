# This works OK
class SequenceGenerator:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('No instance exists. Creating a new one')
            cls._instance = super(SequenceGenerator,cls).__new__(cls)
            cls.sequence = 1
        else:
            print('Previous Instance exists. Using that instance')

        return cls._instance

    # implement methods
    def inc(self):
        self.sequence += 1

    def dec(self):
        self.sequence -= 1

# Instantiate the class
sg = SequenceGenerator()
print(hex(id(sg)))
print(sg.sequence)
sg.inc()
print(sg.sequence)

# try to instantiate class again
# then check the two instances are the same

sg2 = SequenceGenerator()
print(hex(id(sg2)))
print(sg2.sequence)
sg2.dec()
print(sg.sequence)
