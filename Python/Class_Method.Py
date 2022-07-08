"""
todo: In this program, our ibjective is to make a program in python that will IMPLEMENT CLASS METHOD
"""


class student:
    no_of_stu = 5

    def __init__(self, aname, aprofession, asalary):
        self.name = aname
        self.profession = aprofession
        self.salary = asalary

    def student2(self):
        return f"My name is {self.name}"

    @classmethod
    def change_no_of_student(cls, newnumber):
        cls.no_of_stu = newnumber

    @classmethod
    def change_no_of_student2(cls, number):
        cls.no_of_stu = number
        return number


class programmer(student):
    noofjon = 10

    def __init__(self, aname, aprofession, asalary, aage):
        self.name = aname
        self.profession = aprofession
        self.salary = asalary
        self.age = aage

    @classmethod
    def change_no_of_job(cls, number):
        cls.noofjon = number
        return number


Object1 = student("XYZ", "Python Developer", 50000)
print(Object1.profession)
print(Object1.student2())
Object1.change_no_of_student(10)
print(Object1.no_of_stu)
print(student.no_of_stu)
student.change_no_of_student(15)
print(student.no_of_stu)
print(Object1.change_no_of_student2(20))

Object2 = programmer("ABC", "Python Developer", 6000, 21)
print(Object2.__dict__)
print(Object2.change_no_of_job(19))
print(Object2.no_of_stu)
print(programmer.noofjon)
print('\nHit Enter to End.......')
input()
