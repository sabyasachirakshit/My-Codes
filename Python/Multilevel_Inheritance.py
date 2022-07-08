"""
? In this program, we have implemented Multilevel inheritance of class!
! Multilevel Inheritance means when one child class inherits from one parent class that inherits from another parent class..
"""


class university:
    def get_u_details(self):
        self.uname = input('Enter University Name:')
        self.rid = input('Enter Reg. ID [University]::')

    def show_u_details(self):
        print('University Name:', self.uname)
        print('University Reg ID:', self.rid)


class college(university):  # ! INHERITING FROM PARENT CLASS
    def get_clg_details(self):
        self.cname = input('Enter College Name:')
        self.crid = input('Enter Reg. ID [College]:')
        self.get_u_details()

    def show_clg_details(self):
        print('College Name:', self.cname)
        print('College Reg ID:', self.crid)
        self.show_u_details()


# ! INHERITING FROM PARENT CLASS WHICH IS ITSELF A CHILD CLASS{INHERITING FROM ANOTHER PARENT CLASS}
class Student(college):
    def get_stu_details(self):
        self.sname = input('Enter Student Name:')
        self.sroll = input('Enter Roll number:')
        self.sbranch = input('Enter Branch:')
        self.get_clg_details()

    def show_stu_details(self):
        print('STUDENT  DETAILS')
        print('Student Name:', self.sname)
        print('Student Roll number:', self.sroll)
        print('Branch:', self.sbranch)
        self.show_clg_details()


s = Student()
s.get_stu_details()
s.show_stu_details()
print('\nHit Enter to End.......')
input()
