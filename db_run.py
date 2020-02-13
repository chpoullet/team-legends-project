from db_connect import DBConnection
from db_employees import DBEmployees
from db_customers import DBCustomers
from db_products import DBProducts

employees = DBEmployees()
customers = DBCustomers()


print("Welcome to the interface. What would you like to do?")


while True:
    greeting = input("You are in the home section. Type 'help' for a list of commands:\n").lower().strip()


    if 'help' in greeting:
        print("Type 'employees' to enter the employee section\n"
              "Type 'customers' to enter the customer section\n")


    elif 'employee' in greeting:

        while True:
            employee_input = input("You are in the employee section.\n"
                               "Type 'help' for a list of commands for this section\n").lower().strip()
            if employee_input == 'back':
                break

            elif employee_input == 'help':
                print("Type 'view all' to view all employees \n"
                      "Type 'view employee' to view a specific employee \n"
                      "Type 'back' to go back to the home section\n")

            elif employee_input == 'view all':
                employees.print_allemployees()

            elif employee_input == 'view employee':
                idd = int(input('Input an ID:  '))
                print(employees.read_employerid(idd))

            elif employee_input == 'create employee':
                employees.create_employee()


    elif 'menu' or 'product' in greeting:
        product_input = input("You are in the product section:  \n")

    elif 'customer' in greeting:
        while True:
            customer_input = input("You are in the customer section.\n"
                                   "Type 'help' for a list of commands for this section\n").lower().strip()
            if customer_input == 'back':
                break

            elif customer_input == 'help':
                print("Type 'view all' to view all customers\n"
                      "Type 'view customer' to view a singular customer\n"
                      "Type 'back' to go to the home section\n")

            elif customer_input == 'view all':
                customers.print_allcustomers()

            elif customer_input == 'view customer':
                idd = int(input('Input an ID:  '))
                print(customers.read_customerid(idd))





