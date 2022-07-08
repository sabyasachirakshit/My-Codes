"""
!This program is just for practice of all OOPs concept.

?What is Class?
A class is an extensible program code template for creating objects, providing initial values for state and implementations of behaviour
?What is an object?
An object is an abstract data type created by the programmer which possess propoerties, methods and even other objects as well.
?What is Constructor?
Constructor is basically a default class method that assigns value to the instance variable of class.
?What is instance variable of class?
Instance is an individual object of a certain class.
?What is class method?
A class method is a decorator that is used when we only want to work with the class variables and not the instance variables.
When we apply class method as decorator, the function doesn't takes object as an argument, rather it takes cls as argument and cls means class.
?What is  static method?
A static method is a decorator that is used when we want to use a normal function inside a class that doesn't takes self or cls as argumnet.
?What is magic/dunder method?
Dunder methods are nothing but built in functions that can be also used in a class to override methods.
Example--> __add__(), __repr__(), __iter__(), __str__()
?What is property decorator?
It's a decorator that is used to see a function as an attribute
?What is setter decorator?
It's a decorator that is used to set the variables and reflect changes
?What is deleter decorator?
It's a decorator that is being called when we use the del keyword..it just basically deletes an object.
In OOP, we dont delete, we just set values to None.
"""
# ?Classes,Objects and constructors~~~~~~


class Employee:
    increment = 1.5  # ! Class Variable
    no_of_employees = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary  # !Personal Instance Variable
        self.increment = 0.5
        #! self.email = fname+lname+'@email.com'  'This will not reflect changes if we try to access the changed mail after changing fname or lname'
        Employee.no_of_employees += 1

    @classmethod
    def from_str(cls, string):  # ! Class method as alternative constructor..
        fname, lname, salary = string.split("-")
        return cls(fname, lname, salary)

    def increase(self):
        self.salary *= Employee.increment

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

    @staticmethod
    def is_open(day):
        if day.title() == "Sunday":
            return False
        else:
            return True

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return 'Email not Found!!!!'
        else:
            return self.fname+'.'+self.lname+"@email.com"

    @email.setter
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        print(name_list)
        self.fname = name_list[0]
        self.lname = name_list[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

    def __add__(self, other):
        return self.salary+other.salary

    def __repr__(self):
        return f"Employee --> FirstName={self.fname}, LastName={self.lname}, Salary={self.salary}\n"

    def __str__(self):
        return f"The name of the Employee is:{self.fname}"


class Programmer(Employee):
    def __init__(self, fname, lname, salary, prolang, exp):
        super().__init__(fname, lname, salary)
        self.prolang = prolang
        self.exp = exp

    def increase(self):
        self.salary = int(self.salary*(self.increment*2.5))
        return self.salary


if __name__ == "__main__":
    print('No. of employees before calling two objects:', Employee.no_of_employees)
    Jacob = Programmer("Jacob", "Frye", 70000, "C++", '5 yrs')
    print(Jacob.fname, Jacob.lname, Jacob.salary, Jacob.prolang, Jacob.exp)
    print(Jacob.increase())
    Sabyasachi = Employee("Sabyasachi", "Rakshit", 25000)
    Afridi = Employee("SK MD", "Afridi", 25000)
    Ronit = Employee.from_str("Ronit-Basak-30000")
    Alex = Employee("Alex", "Dorain", 3000)
    Ronit.lname = 'Dorain'
    print(Ronit.email)
    Ronit.email = 'Dorain.Ronit@email.com'
    print(Ronit.email)
    print(Alex.is_open("sunday"))
    print(Jacob.email, '\n', Sabyasachi.email)
    print('No. of employees after calling two objects:', Employee.no_of_employees)
    Employee.change_increment(2)
    Sabyasachi.increase()
    print(int(Sabyasachi.salary))
    print(Sabyasachi, Afridi)
    print(Ronit.salary, Ronit.lname, Ronit.fname)
    print(Sabyasachi+Afridi)
    print(Sabyasachi)
    print(str(Afridi))
    # ? To see all the personalinstance variables of an object
    print(Sabyasachi.__dict__)
    # ? To see all the instance variables of an object
    print(Employee.__dict__)
    print(Afridi.lname, Afridi.fname, Afridi.salary)
    print(Sabyasachi.lname, Sabyasachi.fname, Sabyasachi.salary)
    del Jacob.email
    print(Jacob.email)
