class Participants():
    def __init__(self):
        self.__participants = []
        self.__index = 0

    def add_participant(self,name):
        self.__participants.append(name)

    def __len__(self):
        return len(self.__participants)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index == len(self.__participants):
            raise StopIteration

        p = self.__participants(self.__index)

        self.__index += 1

        return p

participants = Participants()
participants.add_participant('Lilly')
participants.add_participant('James')
participants.add_participant('Harry')

#print('for loop\n')
#for p in participants:
#    print(p)

iter(participants)
next(participants)
next(participants)

