
from db_connect import *

class DBProducts(DBConnection):

    def __init__(self):
        super().__init__()
        self.table = 'Customers'


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

