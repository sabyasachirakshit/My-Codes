class student:
    No_Of_Stu=5
    def __init__(self,aname,aprofession,asalary):
        self.name=aname
        self.profession=aprofession
        self.salary=asalary
    def student2(self):
        return f"My name is {self.name}"

    @classmethod
    def change_no_of_student(cls,newNumber):
        cls.No_Of_Stu=newNumber

    @classmethod
    def change_no_of_student2(cls,number):
        cls.No_Of_Stu=number
        return number
class programmer(student):
    noofjon = 10
    def __init__(self,aname,aprofession,asalary,aage):
        self.name=aname
        self.profession=aprofession
        self.salary=asalary
        self.age=aage

    @classmethod
    def change_no_of_job(cls, number):
        cls.noofjon = number
        return number
Afridi=student("SK MD AFRIDI","Python Developer",50000)
print(Afridi.profession)
print(Afridi.student2())
Afridi.change_no_of_student(10)
print(Afridi.No_Of_Stu)
print(student.No_Of_Stu)
student.change_no_of_student(15)
print(student.No_Of_Stu)
print(Afridi.change_no_of_student2(20))

Ronit=programmer("Ronit Basak","Python Developer",6000,21)
print(Ronit.__dict__)
print(Ronit.change_no_of_job(19))
print(Ronit.No_Of_Stu)
print(programmer.noofjon)