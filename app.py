from datetime import datetime
import sys
import traceback

from models import Programmer, Recruiter, Vacancy, Candidate
from unable_to_work_exception import UnableToWorkException

def main():
    employee_1 = Programmer('Alinka', 'ddd@gmail.com', 100, ['Python', 'HTML', 'CSS', 'PostgreSQL'])
    employee_2 = Programmer('Nikita', 'lll@gmail.com', 500,  ['Python', 'GitHub'])
    recruiter_1 = Recruiter('Dasha', 'mmm@gmail.com', 100)
    candidate_1 = Candidate('Maria Klukina', 'mmmkk@gmail.com', ['Python', 'Java Script'], 'Python', 'middle')
    candidate_2 = Candidate('Dima Mironin', 'dima@gmail.com', ['Ruby', 'C#', 'Java'], 'Ruby', 'senior')
    candidate_3 = Candidate('Vladislav Limov', 'vlad@gmail.com', ['HTML', 'CSS', 'C++'], 'C++', 'junior')
    vacancy_1 = Vacancy('Python Developer', 'Python', 'middle')
    vacancy_2 = Vacancy('Ruby Developer', 'Ruby', 'senior')
    # candidate_1.work()
    # print(recruiter_1.full_info)
    # print(employee_1.full_info)
    # print(Candidate.from_csv('candidates.csv'))
    print(Candidate.from_csv('https://bitbucket.org/ivnukov/lesson2/raw/master/candidates.csv'))


if __name__ == '__main__':
    try:
        main()
    except(ValueError, UnableToWorkException) as err:
        tb = sys.exc_info()[2]
        error_class = err.__class__.__name__
        tbinfo = traceback.format_tb(tb)[0]
        error_message = f'{datetime.now()}: {error_class}, Traceback: {tbinfo}'
        filename = './logs.txt'
        f = open(filename, 'a')
        f.write(str(error_message) + '\n')
        f.close()

