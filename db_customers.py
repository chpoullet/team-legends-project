import pyodbc
from db_connect import *

class DBCustomers(DBConnection):

    def __init__(self):
        super().__init__()
        self.table = 'Customers'


    def read_allcustomers(self):  # return iterable object!
        query = 'SELECT * FROM Customers'
        data = self.sql_query(query)
        return data

    def set_customerid(self):
        id = int(input('Select a Customer ID: '))
        return id

    def read_customerid(self, id):
        query = f"SELECT * FROM Customers WHERE CustomerID = {id}"
        result = self.sql_query(query)
        return result.fetchone()

    def print_allcustomers(self):
        query = 'SELECT * FROM Customers'
        data = self.sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"{record.CustomerID} - {record.FirstName} - {record.LastName} - {record.Address}")





# while True:
#     record = all_customers.fetchone()
#     if record is None:
#         break
#     print(record)    # prints all IDs
#
# customer = table_customers.print_id(2)
# print(customer) # prints specific ID
