class Customer:
    def __init__(self, nm, ad, pn):
        self.__name = nm
        self.__address = ad
        self.__phone = pn

    def setName(name):
        self.__name = name

    def setAddress(address):
        self.__address = address

    def setPhone(phone):
        self.__phone = phone

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getPhone(self):
        return self.__phone