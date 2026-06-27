class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = []

    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.marks.append(mark)
        else:
            print("Invalid Marks")

    def get_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def display_info(self):
        print("Name :", self.name)
        print("Roll :", self.roll)
        print("Marks :", self.marks)
        print("Average :", self.get_average())

name = input("Enter Name : ")
roll = input("Enter Roll No : ")

s = Student(name, roll)

try:
    for i in range(5):
        mark = float(input("Enter Mark : "))
        s.add_mark(mark)

except ValueError:
    print("Invalid Input")

s.display_info()
