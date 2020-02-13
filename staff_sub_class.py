from People_class import *

class Staff(People):
    employee_id = 0

    def __init__(self, role, wage, first_name, last_name):
        super().__init__(first_name, last_name)
        self.role = role
        self.__wage = wage
        self.first_name = first_name
        self.last_name = last_name
        Staff.employee_id += 1 

    def email(self):
        email_fname = self.first_name[0]
        return email_fname + '.' + self.last_name + ".@legendsrest.com"
    
    def get_wage(self):
        return self.__wage

# test
#staff_chief = Staff('id_1', 'chief', 50000, 'Babish', 'Long')
# staff_driver = Staff ('id_1', 'Delivery', 30000, 'Dhann', 'Tapatieto')
#
#print(staff_chief.staff_email)
