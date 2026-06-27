def manage_marks():
    marks = []

    try:
        for i in range(5):
            m = float(input("Enter Marks : "))
            marks.append(m)

        print("Average :", sum(marks)/len(marks))
        print("Highest :", max(marks))
        print("Lowest :", min(marks))

        marks.sort(reverse=True)
        print("Descending Order :", marks)

    except ValueError:
        print("Invalid Input")

manage_marks()
