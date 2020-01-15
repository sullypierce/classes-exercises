class Employee:
    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

class Company:
    def __init__(self, name, address, industry):
        self.name = name
        self.address = address
        self.industry = industry
        self.employees = list()

    def hire_employee(self, new_employee):
        self.employees.append(new_employee)

    def list_employees(self):
        print(f"{self.name} is in the {self.industry} industry and has the following employees:")
        for employee in self.employees:
            print(employee.name)

Fred = Employee("fred", "t", "today")
Fred2 = Employee("fred2", "t", "today")
Fred3 = Employee("fred3", "t", "today")
Fred4 = Employee("fred4", "t", "today")
Fred5 = Employee("fred5", "t", "today")

a_company = Company("comp", "here", "things")
another_company = Company("inc", "there", "stuff")

a_company.hire_employee(Fred)
a_company.hire_employee(Fred2)
another_company.hire_employee(Fred3)
another_company.hire_employee(Fred4)
another_company.hire_employee(Fred5)

a_company.list_employees()
another_company.list_employees()
 