class Car:
    def __init__(self, y, m):
        self.__year_model = y
        self.__make = m
        self.__currentSpeed = 0

    def accelerate(self):
        self.__currentSpeed += 5

    def brake(self):
        self.__currentSpeed -= 5

    def getSpeed(self):
        return self.__currentSpeed