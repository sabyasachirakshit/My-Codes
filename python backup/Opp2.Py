class student:
    No_Of_Stu=5
    def __init__(self,aname,aprofession,asalary):
        self.name=aname
        self.profession=aprofession
        self.salary=asalary
    def student2(self):
        return f"My name is {self.name}"

    @classmethod
    def change_no_of_student2(cls,number):
        cls.No_Of_Stu=number
        return number
    @staticmethod
    def statcheck():
        print("My Name is afridi")



Afridi=student("SK MD AFRIDI","Python Developer",50000)
print(Afridi.profession)
print(Afridi.student2())
Afridi.change_no_of_student2(10)
print(Afridi.No_Of_Stu)
print(student.No_Of_Stu)
student.change_no_of_student2(15)
print(student.No_Of_Stu)
print(Afridi.change_no_of_student2(20))
student.statcheck()

