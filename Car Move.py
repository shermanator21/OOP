import CarClass as c


def main():
    lightningMcqueen = c.Car(2012, "rdx")

    for i in range(5):
        lightningMcqueen.accelerate()
        print("Speed is " + str(lightningMcqueen.getSpeed()) + " mph")
    for i in range(5):
        lightningMcqueen.brake()
        print("Speed is " + str(lightningMcqueen.getSpeed()) + " mph")


main()