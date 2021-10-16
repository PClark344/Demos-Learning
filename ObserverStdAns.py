# implement observer class
class Event:
    def __init__(self, name):
        self.name = name

class Observer:
    def __init__(self,name):
        self.name = name

    def call(self,event):
        print('{} called to handle {}'.format(self.name,event.name))

class Emitter:
    def __init__(self):
        self.observers = []

    def register(self,observer):
        self.observers.append(observer)

    def dispatch(self, event):
        for obs in self.observers:
            obs.call(event) 

# attach the observer to an event
# trigger the attached event
# output the results from the observer to verify event was observed
emitter = Emitter()
observer = Observer('Steve')
emitter.register(observer)
emitter.register(Observer('Alice'))

emitter.dispatch(Event('Jump'))
emitter.dispatch(Event('Run'))
emitter.dispatch(Event('Click'))
emitter.dispatch(Event('Press'))
