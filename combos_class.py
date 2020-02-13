from food_class import *
from drink_class import *

food_menu = [(1, 'Pizza', 6.50, 'Meal'), (2, 'Lasagna', 7.00, 'Meal'), (3, 'Ravioli', 5.50, 'Meal'),
             (4, 'Soup', 4.00, 'Meal'), (5, 'Spaghetti', 6.00, 'Meal')]
drinks_menu = [(1, 'Coke', 2.50, 'Meal'), (2, 'Water', 1.50, 'Meal'), (3, 'Prosecco', 5.00)]
sides_menu = [(1, 'Garlic Bread', 3.50, 'Meal'), (2, 'Mozzerella sticks', 3.50, 'Meal'), (3, 'Fries', 2.50, 'Meal'),
              (4, 'Jalapeno poppers', 4.50, 'Other')]
discount_rate = 0.5


# class Combos():
def __init__(self, name, price):
    super().__init__(name, price)
    self.name = name
    self.price = price


def combo_discount():
    for j in food_menu:
        for k in drinks_menu:
            if j[3] == 'Meal' and k[3] == 'Meal':
                total = j[1] + k[1]
                discount = total * discount_rate
                print("{}:{} {}:{} total to pay = £{}, instead of £{}".format(j[0], j[2], k[0], k[2], discount, total))


