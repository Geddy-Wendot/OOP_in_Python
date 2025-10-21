class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print (f"Hi I'm {self.name}, I'm {self.age} years old")
    
class student(Parent):
    def __init__(self, name, age, unit):
        super().__init__(name,age)
        self.unit=unit

    def study(self):
        print(f"{self.name} is studying for his {self.unit} exams")

class teacher(Parent):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject

    def teach(self):
        print(f"{self.name} lectures on {self.subject} this year")

#example use
s= student("Josh", 20, "Mathematics")
t=teacher("Dr Andrew", 40, "Mathematics")

s.introduce()
t.introduce()

s.study()
t.teach()