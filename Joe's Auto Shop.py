import CarClass2 as cr
import CustomerClass as ct
import ServiceQuoteClass as s


def main():
    # getting input from customer
    name, address, phone_num = input(
        "Customer, please enter your name, address, and phone number (seperated by spaces): "
    ).split()

    # creating a customer class instance
    Customer = ct.Customer(name, address, phone_num)

    # getting car info from manager
    make, model, year = input(
        "Manager, please enter the make, model, and year of your car (seperated by spaces): "
    ).split()

    # creating a car class instance
    Car = cr.Car(make, model, year)

    # getting charge info from manager and converting it into usable data
    pcharge, lcharge = input(
        "Manager, please enter the estimated part charges as well as the estimated labor charges (seperated by spaces): "
    ).split()

    if "$" in pcharge:
        pcharge = pcharge.lstrip("$")

    if "$" in lcharge:
        lcharge = lcharge.lstrip("$")

    # creating service quote class instance
    ServiceQuote = s.ServiceQuote(pcharge, lcharge)

    # getting sales tax and total charge
    salesTax = ServiceQuote.get_sales_tax()
    totalCharge = ServiceQuote.get_total_charges()

    # outputing the service quote for the customer
    print(
        "Your estimated parts charge is $"
        + str(ServiceQuote.get_parts_charges())
        + ", your estimated labor charge is $"
        + str(ServiceQuote.get_labor_charges())
        + ", your sales tax is "
        + str(ServiceQuote.get_sales_tax() * 100)
        + "%, and your total charge is $"
        + str(ServiceQuote.get_total_charges())
        + "."
    )


main()