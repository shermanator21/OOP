import RetailClass as r


def main():

    myItems = {}

    # Item 1
    description = "Jacket"
    units = 12
    price = 59.95
    myItems[0] = r.RetailItem(description, units, price)

    # Item 2
    description = "Designer Jeans"
    units = 40
    price = 34.95
    myItems[1] = r.RetailItem(description, units, price)

    # Item 3
    description = "Shirt"
    units = 20
    price = 24.95
    myItems[2] = r.RetailItem(description, units, price)

    myItems[0].displayItem()

    # for future use if data is unknown
    """
    for i in range(3,6):
        description = input("Please enter the item's description: ")
        units = input("Please enter the number of units in inventory: ")
        price = input("Please input the price of the item: $")
        myTempItem = r.RetailItem(description, units, price)
        myTempItem.displayItem()

        myItems[i] = myTempItem
    """


main()