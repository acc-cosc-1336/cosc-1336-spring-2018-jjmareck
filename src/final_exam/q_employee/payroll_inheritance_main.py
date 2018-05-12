from hourly_employee import HourlyEmployee
from salaried_employee import SalariedEmployee

def main():
    employees = {1:HourlyEmployee(1,'joe',10,80),2:SalariedEmployee(2,'Mike',80000)}
    for key in employees:
        print(employees[key].calculate())

main()

