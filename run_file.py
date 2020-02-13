from food_class import *
# from drink_class import *
# from combos_class import *

# food_menu = [(1, 'Pizza', 6.50, 'Meal'), (2, 'Lasagna', 7.00, 'Meal'), (3, 'Ravioli', 5.50, 'Meal'),
#              (4, 'Soup', 4.00, 'Meal'), (5, 'Spaghetti', 6.00, 'Meal')]
# drinks_menu = [(1, 'Coke', 2.50, 'Meal'), (2, 'Water', 1.50, 'Meal'), (3, 'Prosecco', 5.00)]
# sides_menu = [(1, 'Garlic Bread', 3.50, 'Meal'), (2, 'Mozzerella sticks', 3.50, 'Meal'), (3, 'Fries', 2.50, 'Meal'), (4, 'Jalapeno poppers', 4.50, 'Other')]
# discount_rate = 0.5


main1 = Food('Pizza', 6.50, ['Bread base', 'tomato sauce', 'olives', 'herbs'])
main2 = Food('Lasagna', 7.00, ['Pasta dough', 'Tomato sauce', 'Lamb mince meat'])
main3 = Food('Ravioli', 5.50, ['Tomato sauce', 'spinach', 'cheese'])
main4 = Food('Soup', 4.00, ['diced veggies', 'chicken stock', 'herbs'])
main5 = Food('Spaghetti', 6.00, ['Spaghetti pasta', 'ragu sauce', 'cheese', 'herbs'])
drink1 = Drink('Coke', 2, ['caffeine'])
drink2 = Drink('Smoothie', 2.5, ['orange'])

for i in range (0, len(MenuItems.menu_items_list)):
    print(MenuItems.menu_items_list[i])

