class Publisher:
    def __init__(self,name):
        self.__name = name
        self.__subscribers = set()
   
    def register(self,subscriber):
        self.__subscribers.add(subscriber)

    def unregister(self,subscriber):
        self.__subscribers.discard(subscriber)

    def publish(self,msg):
        for subscriber in self.__subscribers:
            subscriber.notify(msg)

class Subscriber():
    def __init__(self,name):
        self.__name = name

    def notify(self,msg):
        print(self.__name + ' - received message: ',msg)

publisher = Publisher('News')
alice = Subscriber('Alice')
betty = Subscriber('Betty')

publisher.register(alice)
publisher.register(betty)

publisher.publish('No news today')

charles = Subscriber('Charles')
publisher.register(charles)

publisher.publish('Lots of news today')

publisher.unregister(betty)

publisher.publish('Even more news')

