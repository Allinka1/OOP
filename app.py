from models import Programmer, Recruiter, Vacancy, Candidate


if __name__ == '__main__':

    print(__name__)

    employee_1 = Programmer('Alinka', 'ddd@gmail.com', 100, ['Python', 'HTML', 'CSS', 'PostgreSQL'])
    employee_2 = Programmer('Nikita', 'lll@gmail.com', 500,  ['Python', 'GitHub'])
    recruiter_1 = Recruiter('Dasha', 'mmm@gmail.com', 100)
    candidate_1 = Candidate('Maria Klukina', 'mmmkk@gmail.com', ['Python', 'Java Script'], 'Python', 'middle')
    candidate_2 = Candidate('Dima Mironin', 'dima@gmail.com', ['Ruby', 'C#', 'Java'], 'Ruby', 'senior')
    candidate_3 = Candidate('Vladislav Limov', 'vlad@gmail.com', ['HTML', 'CSS', 'C++'], 'C++', 'junior')
    vacancy_1 = Vacancy('Python Developer', 'Python', 'middle')
    vacancy_2 = Vacancy('Ruby Developer', 'Ruby', 'senior')

    print(employee_2.check_salary())
    alfa = Programmer.alfa_programmer(employee_1, employee_2)
    print(alfa.tech_stack)
    print(vacancy_1)
    print(candidate_2)
