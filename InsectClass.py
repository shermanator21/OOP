import random


class Insect:
    def __init__(self):
        self.__wings = 2
        self.__legs = 4

    def flight(self):
        self.__flight = random.randint(0, 10)
