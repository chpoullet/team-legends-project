import pyodbc

first_name = input("Enter the employee's first name: ")
last_name = input("Enter the employee's last name: ")
# customer_address = input('Enter your address: ')
# card_no = input('Input card details:  ')

server = 'localhost,1433'
database = 'Restaurant'
username = 'SA'
password = 'Passw0rd2018'

database_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+username+';PWD='+password)


cursor = database_connection.cursor()
print("INSERT INTO Employees (FirstName, LastName) VALUES (?, ?)",(first_name, last_name))
cursor.execute("INSERT INTO Employees (FirstName, LastName) VALUES (?, ?)",(first_name, last_name))
database_connection.commit()

