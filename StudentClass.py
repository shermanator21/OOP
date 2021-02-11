from datetime import date


class Student:
    def __init__(self, id, n, dob, c):
        self.__studentID = id
        self.__name = n
        self.__dateOfBirth = dob
        self.__classification = c

    def calculateAge(self):
        # First split age into string then re arrange
        birthDate = self.__dateOfBirth.split()
        birthDay = birthDate[1]
        birthMonth = birthDate[0]
        birthYear = birthDate[2]

        # Strip the comma from the entry

        birthDay = birthDay.rstrip(",")
        birthMonth = birthMonth.rstrip(",")
        birthYear = birthYear.rstrip(",")

        # Convert strings to int
        birthDay = int(birthDay)
        birthMonth = int(birthMonth)
        birthYear = int(birthYear)

        # Calculate age based on current day
        today = date.today()
        age = (
            today.year - birthYear - ((today.month, today.day) < (birthMonth, birthDay))
        )
        return age

    def registerRange(self):
        if self.__classification == "F":
            print("Your registration is open 11/10 through 11/12.")
        elif self.__classification == "S":
            print("Your registration is open 11/7 through 11/9.")
        elif self.__classification == "Jr":
            print("Your registration is open 11/4 through 11/6.")
        elif self.__classification == "Sr":
            print("Your registration is open 11/1 through 11/3.")
        else:
            print("Classification not specified.")