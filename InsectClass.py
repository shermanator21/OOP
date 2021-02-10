import random


class Insect:
    def __init__(self, w, l, f):
        self.__wings = w
        self.__legs = l
        self.__flight = f

    # mutator method
    def flightLength(self):
        self.__flight = random.randint(1, 10)
        # could also combine "get_flight" here.

    # accessor methods

    def get_wings(self):
        return self.__wings

    def get_legs(self):
        return self.__legs

    def get_flight(self):
        return self.__flight

    def __str__(self):
        return (
            "wings:"
            + str(self.__wings)
            + "\n"
            + "legs:"
            + str(self.__legs)
            + "\n"
            + "flight:"
            + str(self.__flight)
        )
