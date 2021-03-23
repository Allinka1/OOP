import numpy as np
from datetime import datetime, date, time


class Employee:

    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    def work(self):
        return('I come to the office')

    def check_salary(self):
        today = date.today()
        first_day_of_month = date(today.year, today.month, 1)
        days = np.busday_count(first_day_of_month, today)
        money = self.salary * days + self.salary
        print(money)

    def compare_salary(self, another_employee):
        if self.salary > another_employee.salary:
            sign = '>'
        elif self.salary < another_employee.salary:
            sign = '<'
        else:
            sign = '='
        return(f'Salary of {self.name} {sign} salary of {another_employee.name}')


class Programmer(Employee):

    def __init__(self, name, email, salary, tech_stack):
        super().__init__(name, email, salary)
        self.tech_stack = tech_stack

    def work(self):
        return(f'{super().work()} and start to coding')

    def __str__(self):
        return(f'Programmer: {self.name}')

    def compare_teches(self, another_employee):

        if len(self.tech_stack) > len(another_employee.tech_stack):
            sign = '>'
        elif len(self.tech_stack) < len(another_employee.tech_stack):
            sign = '<'
        else:
            sign = '='
        return(f'Tech stack of {self.name} {sign} tech stack of {another_employee.name}')

    def alfa_programmer(*args):
        alfa_tech_stack = set()
        for i in args:
            alfa_tech_stack = alfa_tech_stack.union(set(i.tech_stack))
        alfa_programmer = Programmer('Alfa', 'alfa@gmail.com', 1000, list(alfa_tech_stack))
        return alfa_programmer


class Recruiter(Employee):

    def work(self):
        return(f'{super().work()} and start to hiring')

    def __str__(self):
        return(f'Recruiter: {self.name}')


class Candidate:

    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade


class Vacancy:

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level
