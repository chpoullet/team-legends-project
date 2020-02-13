from People_class import People


class Customer(People):
    customer_id = 0
    def __init__(self, first_name, last_name, address=None):
        super().__init__(first_name, last_name)
        if address is None:
            address = []
        else:
            self.address = address
        self.__payment_details = {}
        self.first_name = first_name
        self.last_name = last_name
        Customer.customer_id += 1

    def set_payment_details(self, address, card_no):
        self.__payment_details['address'] = address
        self.__payment_details['card number'] = card_no

    def get_payment_details(self):
        return self.__payment_details

# address details , payment details
# alter ingredient
# combo method?
