# create two classes to instantiate factory pattern
# create a factory class with methods to instantiate objects
class Action:
    def do(action):
        if action == 'push':
            return Push()
        elif action == 'pull':
            return Pull()

    do = staticmethod(do)

class Push(Action):
    def act(self):
        print('Pushing!')

class Pull(Action):
    def act(self):
        print('Pulling!')

# Instantiate the object factory and call its methods
# output the results of the instantiated objects
action = Action.do('push')
action.act()

action = Action.do('pull')
action.act()

