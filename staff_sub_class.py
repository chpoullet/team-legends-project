from People_class import *

class Staff(People):

    def __init__(self, employee_id, role, wage, first_name, last_name):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id
        self.role = role
        self.__wage = wage
        self.first_name = first_name
        self.last_name = last_name
        self.staff_email = self.first_name + '.' + self.last_name + ".@restautant.com"



staff_chief = Staff('id_1', 'chief', 50000, 'Babish', 'Long')
staff_driver = Staff ('id_1', 'Delivery', 30000, 'Dhann', 'Tapatieto')

print(staff_chief.staff_email)
