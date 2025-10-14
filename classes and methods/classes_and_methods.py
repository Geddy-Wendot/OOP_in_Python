#Classes: a blueprint in creating objects
#Objects: An instance of a class

#simple student class

class Student:
    def __init__(self,name,age):
        #attributes
        self.name=name
        self.age=age

    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old.")

#creates the object
student1=Student("Allice",20)
student2=Student("John",27)

#calls the method
student1.greet()
student2.greet()


#calculate area of a circle
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.142*self.radius**2
   
circle=Circle(45)
print(f"Area is: {circle.area()}")

'''Exercise: The Student Class

Goal:
Build a class called Student that models a student with a name, age, and list of grades.

Requirements:

The class should initialize with name, age, and an empty list for grades.

Add a method add_grade(self, grade) to append a grade (0–100).

Add a method average(self) that returns the average grade (or 0 if there are none).

Add a method info(self) that returns a string like:
"Name: Geddy, Age: 20, Average: 85.6"'''

class Students:
    def __init__(self, name, age, grade=None):
        self.name = name
        self.age = age
        self.grade =[] if grade is None else list(grade)

    def add_grade(self,grade):
        if not isinstance(grade,(int,float)):
            raise TypeError("grade must be a number")
        if grade < 0 or grade > 100:
            raise ValueError("grade must be between 0 to 100")
        self.grade.append(float(grade))

    def average(self):
        return sum(self.grade)/len(self.grade)
    
    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Average: {self.average(): .2f}"
    
s=Students("Geddy", 20)
s.add_grade(90.1)
s.add_grade(83.3)
print(s.info())



    