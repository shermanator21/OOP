class Car:
    def __init__(self, mk, md, y):
        self.__make = mk
        self.__model = md
        self.__year = y

    def setMake(make):
        self.__make = make

    def setModel(model):
        self.__model = model

    def setYear(year):
        self.__year = year

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getYear(self):
        return self.__year