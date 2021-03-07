class ServiceQuote:
    def __init__(self, p, l):
        self.__pcharge = p
        self.__lcharge = l
        self.__salesTax = 0.0625

    def set_parts_charges(pcharge):
        self.__pcharge = pcharge

    def set_labor_charges(lcharge):
        str(lcharge)
        if "$" in lcharge:
            lcharge = lcharge.lstrip("$")
        print(lcharge)
        self.__lcharge = lcharge

    def set_sales_tax(salesTax):
        self.__salesTax = salesTax

    def get_parts_charges(self):
        return self.__pcharge

    def get_labor_charges(self):
        return self.__lcharge

    def get_sales_tax(self):
        return self.__salesTax

    def get_total_charges(self):
        return (float(self.__pcharge) + float(self.__lcharge)) + (
            (float(self.__pcharge) + float(self.__lcharge)) * self.__salesTax
        )
