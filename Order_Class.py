class Order():
    food = {'pizza': 20,
            'pasta': 30}
    order_count = 0

    def __init__(self, customer):
        self.items = []
        self.customer = customer
        self.status = 'Open'
        self.order_count = 0

    # ===================================================
    # Based on the customer input, add item to self.items
    # ===================================================
    def add_item_order(self):
        self.items.append(self.customer)

        while self.order_count < 3:
            self.item = input("What would you like to order: ")
            self.items.append(self.item)
            self.order_count += 1
        print(self.items)
    # ===================================================
    # Loop through self.item skipping index 1 and retrieve
    # all the data based on the Key
    # ===================================================
    def total_price(self):
        total = 0
        if self.item in Order.food.keys():
            for item in self.items[1::]:
                total = total + Order.food[item]
            print(total)
    # ===================================================
    # Optional: search and Retrieve customer order
    # ===================================================
    def search_customer(self):
        self.customer = input('what customer do you want?')
        if self.customer in self.items:
            print(self.items)



# customer1 = Order('Hamza')
# customer1.add_item_order()
# customer1.total_price()
# customer1.search_customer()
# print(customer1.items)
# #
# # customer2 = Order('Jason')
# # customer2.add_item_order()
# # customer2.total_price()
#
# customer1.search_customer()
# # customer2.search_customer()
#
# print(customer1.items)
# # print(customer2.items)