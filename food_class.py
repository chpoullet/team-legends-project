class MenuItems:
    menu_items_list = []

    def __init__(self, name, price, ingredients=None):
        self.name = name
        self.price = price
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients
        MenuItems.add_menu_item_to_list(self)

    @classmethod
    def add_menu_item_to_list(cls, item):
        cls.menu_items_list.append(item)


class Drink(MenuItems):
    drink_items_list = []

    def __init__(self, name, price, ingredients=None):
        super().__init__(name, price, ingredients)
        Drink.add_drink_item(self)

    @classmethod
    def add_drink_item(cls, item):
        cls.drink_items_list.append(item)


class Food(MenuItems):
    food_items_list = []

    def __init__(self, name, price, ingredients=None):
        super().__init__(name, price, ingredients)
        Food.add_food_item(self)

    @classmethod
    def add_food_item(cls, item):
        cls.food_items_list.append(item)

# food_menu = [(1, 'Pizza', 6.50, 'Meal'), (2, 'Lasagna', 7.00, 'Meal'), (3, 'Ravioli', 5.50, 'Meal'),
#              (4, 'Soup', 4.00, 'Meal'), (5, 'Spaghetti', 6.00, 'Meal')]

# main1 = Food('Pizza', 6.50, ['Bread base', 'tomato sauce', 'olives', 'herbs'])
# main2 = Food('Lasagna', 7.00, ['Pasta dough', 'Tomato sauce', 'Lamb mince meat'])
# main3 = Food('Ravioli', 5.50, ['Tomato sauce', 'spinach', 'cheese'])
# main4 = Food('Soup', 4.00, ['diced veggies', 'chicken stock', 'herbs'])
# main5 = Food('Spaghetti', 6.00, ['Spaghetti pasta', 'ragu sauce', 'cheese', 'herbs'])
#
# print(food_items_list)
