"""
? In this program, we have implemented multiple inheritance of class!
! Multiple Inheritance means when one child class inherits from multiple parent class..
"""


class cement_dealer:
    def get_cement_cost(self, quantity):
        return quantity*300


class iron_dealer:
    def get_iron_cost(self, quantity):
        return quantity*4500


class builder(cement_dealer, iron_dealer):  # ! Multiple Inheritance
    def get_total_cost(self, cq, iq):
        c_cost = self.get_cement_cost(cq)
        i_cost = self.get_iron_cost(iq)
        t_cost = c_cost+i_cost
        return t_cost


cement = int(input('Enter Cement Quantity:'))
iron = int(input('Enter Iron Quantity:'))
b = builder()
total_cost = b.get_total_cost(cement, iron)
print("Total Cost:", total_cost)
print('\nHit Enter to End.......')
input()
