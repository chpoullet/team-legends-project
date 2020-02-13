class Order():
    item1 = {
        'name': 'pizza',
        'price': 2.4
    }
    item2 = {
        'name': 'cocacola',
        'price': 1.4
    }
    item3 = {
        'name': 'tiramisu',
        'price': 3.4
    }
    list_items = [item1, item2, item3]

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
        while True:

            self.item = input("What would you like to order: ")
            self.items.append(self.item)
            if self.item == '':
                break
        print(f'{self.items}')

    # ===================================================
    # Loop through self.item skipping index 1 and retrieve
    # all the data based on the Key
    # ===================================================
    def total_price(self):
        total = 0
        # get the items from the instance
        # iterate
        # from each item, get the price
        # addit to a counter
        # return
        for item in Order.list_items:
            total += item['price']
        print(f'Your Total is: {round(total)}')

    # ===================================================
    # Optional: search and Retrieve customer order
    # ===================================================
    # def search_customer(self):
    #     self.customer = input('what customer do you want?')
    #     if self.customer in self.items:
    #         print(self.items)


customer1 = Order('Hamza')
customer1.add_item_order()
customer1.total_price()
