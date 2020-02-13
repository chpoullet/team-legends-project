from db_connect import *

class DBEmployees(DBConnection):

    def __init__(self):
        super().__init__()
        self.table = 'Employees'


    def sql_query(self, sql_query, args = None):
        if args == None:
            return self.cursor.execute(sql_query)
        else:
            return self.cursor.execute(sql_query, args)


    def read_allemployees(self):
        query = 'SELECT * FROM Employees'
        data = self.sql_query(query)
        return data


    def set_employeeid(self):
        id = int(input('Select an Employee ID: '))
        return id


    def read_employerid(self, id):
        query = f"SELECT * FROM Employees WHERE EmployeeID = {id}"
        result = self.sql_query(query)
        return result.fetchone()


    def print_allemployees(self):
        query = 'SELECT * FROM Employees'
        data = self.sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"{record.EmployeeID} - {record.FirstName} - {record.LastName} - {record.JobRole} - £{record.Wage}")


    def create_employee(self):
        first_name = str(input("Enter the employee's first name: "))
        last_name = str(input("Enter the employee's last name:  "))
        jobrole = str(input("Enter the employee's job role:   "))
        wage = int(input("Enter the employee's wage:   "))
        query = "INSERT INTO Employees (FirstName, LastName, JobRole, Wage) VALUES (?, ?, ?, ?)"
        args = (first_name, last_name, jobrole, wage)
        self.sql_query(query, args)
        self.docker_Restaurant.commit()


# table_employees = DBEmployees()
# employee_row = table_employees.print_employeerow()
# allemployees = table_employees.print_allemployees()
# table_employees = DBEmployees()
# all_employees = table_employees.print_allemployees()

#     def print_employeerow(self):

    # row = input("What row would you like to view?   ")
    #     query = f"SELECT {row} FROM Employees"
    #     data = self.sql_query(query)
    #     while True:
    #         record = data.fetchone()
    #         if record is None:
    #             break
    #         print(f"{?????}")
