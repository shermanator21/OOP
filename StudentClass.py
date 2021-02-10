from datetime import date


class Student:
    def __init__(self, id, n, dob, c):
        self.__studentID = id
        self.__name = n
        self.__dateOfBirth = dob
        self.__classification = c

    def calculateAge(self):
        today = date.today()
        age = today - self.__dateOfBirth
        return age

    def registerRange(self):
        if self.__classification == "freshman":
            #display range
        else if:

        else if:

        else: