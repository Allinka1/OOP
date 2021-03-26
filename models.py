from datetime import datetime, date, time
import numpy as np
import urllib.request
from unable_to_work_exception import UnableToWorkException


class Employee:

    def save_email(self):
        filename = './emails.txt'
        f = open(filename, 'a')
        f.write(str(self.email) + '\n')
        f.close()

    def validate_email(self):
        filename = './emails.txt'
        f = open(filename, 'r')
        for stored_email in f:
            print(stored_email)
            if stored_email.replace("\n", "") == self.email:
                raise ValueError('This email exists, please enter a new one')
        f.close()

    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary
        # self.validate_email()
        # self.save_email()


    def work(self):
        return('I come to the office')

    def check_salary(self):
        # today = date.today()
        # first_day_of_month = date(today.year, today.month, 1)
        days = work_days()
        money = self.salary * days + self.salary
        return money

    @staticmethod
    def work_days():
        today = date.today()
        first_day_of_month = date(today.year, today.month, 1)
        return np.busday_count(first_day_of_month, today) + 1

    def compare_salary(self, another_employee):
        if self.salary > another_employee.salary:
            sign = '>'
        elif self.salary < another_employee.salary:
            sign = '<'
        else:
            sign = '='
        return(f'Salary of {self.name} {sign} salary of {another_employee.name}')

    @property
    def full_info(self):
        return f'Class: {self.__class__.__name__}\nName: {self.name}\nWork Days: {self.work_days()}\n{"-" * 15}'


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

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return(f'Candidate: {self.full_name}, {self.email}, {self.technologies}, {self.main_skill}, {self.main_skill_grade}')

    @classmethod
    def from_csv(cls, csv):
        result = []
        try:
            data_file = open(csv)
        except(FileNotFoundError):
            data_file = urllib.request.urlopen(csv)
        lines = data_file.readlines()[1:]
        for row in lines:
            if csv.startswith('http'):
                candidate_data = row.decode("utf-8").split(",")
            else:
                candidate_data = row.split(",")
            full_name = candidate_data[0]
            email = candidate_data[1]
            technologies = candidate_data[2].split("|")
            main_skill = candidate_data[3]
            main_skill_grade = candidate_data[4]
            result.append(cls(full_name, email, technologies, main_skill, main_skill_grade))
        return result

    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    # def work(self):
    #     print(UnableToWorkException)
    #     raise UnableToWorkException('I’m not hired yet, lol')


class Vacancy:

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level
