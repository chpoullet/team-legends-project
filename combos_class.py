from food_class import *
main1 = Food('Pizza', 6.50, ['Bread base', 'tomato sauce', 'olives', 'herbs'])
main2 = Food('Lasagna', 7.00, ['Pasta dough', 'Tomato sauce', 'Lamb mince meat'])
main3 = Food('Ravioli', 5.50, ['Tomato sauce', 'spinach', 'cheese'])
main4 = Food('Soup', 4.00, ['diced veggies', 'chicken stock', 'herbs'])
main5 = Food('Spaghetti', 6.00, ['Spaghetti pasta', 'ragu sauce', 'cheese', 'herbs'])
drink1 = Drink('Coke', 2, ['caffeine'])
drink2 = Drink('Smoothie', 2.5, ['orange'])

# class Order:
#     def __init__(self, customer, order_id

class Order:
    __order_integer = 1

    def __init__(self, customer, order_id):
        self.customer = customer
        self.order_id = Order.__order_integer
        Order.__order_integer += 1
        self.order_contents = []

    # def combo_discount(self):
    #     if self.order_contents :
    #         for k in drinks_menu:
    #         discount_rate = 0.2
    #         if j[3] == 'Meal' and k[3] == 'Meal':
    #             total = j[2] + k[2]
    #             discount = total * discount_rate
    #             print("{}:{} {}:{} total to pay = £{}, instead of £{}".format(j[0], j[2], k[0], k[2], discount, total))


# if order contains an object 'Food' and an object 'Drink'
# apply 20% discount





#         food_menu = [Food(1, 'Pizza', 6.50, 'Meal'), Food(2, 'Lasagna', 7.00, 'Meal'), Food(3, 'Ravioli', 5.50, 'Meal'),
#                      Food(4, 'Soup', 4.00, 'Meal'), Food(5, 'Spaghetti', 6.00, 'Meal')]
#         drinks_menu = [(1, 'Coke', 2.50, 'Meal'), (2, 'Water', 1.50, 'Meal'), (3, 'Prosecco', 5.00)]
#         sides_menu = [(1, 'Garlic Bread', 3.50, 'Meal'), (2, 'Mozzerella sticks', 3.50, 'Meal'), (3, 'Fries', 2.50, 'Meal'),
#                       (4, 'Jalapeno poppers', 4.50, 'Other')]
#
#
# pizza = Food('Pizza', 6.5, 'None')



