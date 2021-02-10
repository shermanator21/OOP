import InsectClass as i


def main():
    my_insect = i.Insect(2, 4, 0)
    print(my_insect)

    # Determine flight length
    my_insect.flightLength()

    # Print length of flight
    print("The insect can fly up to " + str(my_insect.get_flight()) + " miles.")


main()
