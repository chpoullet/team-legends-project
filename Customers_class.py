from People_class import People


class Customer(People):
    #keeping track of things
    customer_id = 0
    customer_db = []

    # the thing
    def __init__(self, first_name, last_name, address=None):
        super().__init__(first_name, last_name)
        if address is None:
            address = []
        self.address = address
        self.__payment_details = {}
        self.first_name = first_name
        self.last_name = last_name
        self.id_cst = Customer.customer_id
        Customer.customer_id += 1



    def set_payment_details(self, address, card_no):
        self.__payment_details['address'] = address
        self.__payment_details['card number'] = card_no

    def get_payment_details(self):
        return self.__payment_details

    def get_cst_id(self):
        return self.id_cst

    @classmethod
    def print_all_customers(cls):
        for cst in cls.customer_db:
            print(f'{cst.get_cst_id()}- {cst.first_name} ')

# Test Customer class
# from Customers_class import Customer
#
# while True:
#
#     print('\n What would to like to do?\n'
#           'type \"help\" for command list')
#     what_action_input = input('>>>>')
#
#     if what_action_input == '1' or what_action_input == 'create customer' in what_action_input:
#         print('Creating a customer')
#
#         first_name = input('What is your first name? \n')
#         last_name = input('What is your last name?\n')
#         cst_address = input('Address:\n ')
#         cst_post_code = input('Postcode: \n')
#         cst_dets = Customer(first_name, last_name, [cst_address, cst_post_code])
#         # create the custer
#         # append to empty list
#         # breakpoint()
#         cst_dets.customer_db.append(cst_dets)
#
#         Customer.print_all_customers()