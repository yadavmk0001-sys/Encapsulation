class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
    
    def display(self):
        print(self.roll, self.name, self.marks)
    
student = []
def add_student():
    roll = int(input("Enter roll no.: "))
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    student.append(Student(roll, name, marks))

def view_student():
    for s in student:
        s.display()
    
while True:
    print("\n1.Add Student: \n2.View Student: \n3.Exit")
    choice = input("Enter choice : ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        break
    else:
        print("Invalid choice")