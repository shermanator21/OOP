import InsectClass as i


def main():
    my_insect = i.Insect()

    # Determine flight length
    my_insect.newFlight()

    # Print length of flight
    print("The insect can fly " + str(my_insect.get_flight()) + " miles.")


main()
