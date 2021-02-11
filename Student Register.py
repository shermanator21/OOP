import StudentClass as s


def main():
    stu_id = input("Please enter your student ID: ")
    name = input("Please enter your name: ")
    dob = input("Please enter your date of birth (month, day, year): ")
    cl = input("Please enter your classification (F, S, Jr, or Sr): ")

    my_student = s.Student(stu_id, name, dob, cl)

    print("Your age is " + str(my_student.calculateAge()) + ".")

    my_student.registerRange()


main()