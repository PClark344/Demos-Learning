# This works OK
class Logger:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('No instance exists. Creating a new one')
            cls._instance = super(Logger,cls).__new__(cls)
        else:
            print('Previous Instance exists. Using that instance')

        return cls._instance

# Instantiate the class
lg1 = Logger()
print(hex(id(lg1)))

# try to instantiate class again
# then check the two instances are the same
lg1 = Logger()
print(hex(id(lg1)))


