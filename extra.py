class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        
s1 = student("Pragya", 13)
s2 = student("Sonali", 22)

s1.display()
s2.display()