class RetailItem:
    def __init__(self, d, u, p):
        self.__description = d
        self.__units_in_inventory = u
        self.__price = p

    def displayItem(self):
        print(
            "\nDescription: "
            + self.__description
            + "\nUnits in Inventory: "
            + str(self.__units_in_inventory)
            + "\nPrice: $"
            + str(self.__price)
        )
