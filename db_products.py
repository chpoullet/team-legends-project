
from db_connect import *

class DBProducts(DBConnection):

    def __init__(self):
        super().__init__()
        self.table = 'Customers'

    def sql_query(self, sql_query, args = None):
        if args == None:
            return self.cursor.execute(sql_query)
        else:
            return self.cursor.execute(sql_query, args)

    def read_allproducts(self):
        query = 'SELECT * FROM Products'
        data = self.sql_query(query)
        return data


    def set_productid(self):
        id = int(input('Select a Product ID:'))
        return id


    def read_productid(self, id):
        query = f"SELECT * FROM Products WHERE ProductID = {id}"
        result = self.sql_query(query)
        return result.fetchone()


    def print_allproducts(self):
        query = 'SELECT * FROM Products'
        data = self.sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"{record.ProductID} - {record.ProductName} - {record.Category} - {record.Price}")


    def create_product(self):
        product_name = str(input("Enter the product name:  "))
        category = str(input("Enter the product category (beverage/food):  "))
        price = int(input("Enter the price for the product:  "))
        query = "INSERT INTO Products (ProductName, Category, Price) VALUES (?, ?, ?)"
        args = (product_name, category, price)
        self.sql_query(query, args)
        self.docker_Restaurant.commit()
