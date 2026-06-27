def student_database():
    students = {}

    while True:
        print("\n1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            city = input("Enter City: ")

            students[roll] = {
                "Name": name,
                "Age": age,
                "City": city
            }

        elif choice == "2":
            roll = input("Enter Roll No: ")
            print(students.get(roll, "Student Not Found"))

        elif choice == "3":
            for roll, data in students.items():
                print(roll, data)

        elif choice == "4":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

student_database()
