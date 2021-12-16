from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

def calculate():
    if __name__ == '__main__':
        calculate_salary()
        print(datetime.today())

def get():
    if __name__ == '__main__':
        get_employees()
        print(datetime.today())

        
get()
calculate()

