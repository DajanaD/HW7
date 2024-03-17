from faker import Faker
from models import Student, Group, Teacher, Subject, Grade
from random import randint, choice
from connect_db import session

# Ініціалізація Faker
fake = Faker()

# Створення груп
groups = [Group(name=f'Group {i}') for i in range(1, 4)]
session.add_all(groups)
session.commit()

# Створення викладачів
teachers = [Teacher(name=fake.name()) for _ in range(3)]
session.add_all(teachers)
session.commit()

# Створення студентів та прив'язка їх до груп
students = []
for _ in range(30, 51):
    student = Student(name=fake.name(), group=choice(groups))
    students.append(student)
session.add_all(students)
session.commit()

# Створення предметів та призначення їх викладачам
subjects = []
for _ in range(5, 9):
    subject = Subject(name=fake.catch_phrase(), teacher=choice(teachers))
    subjects.append(subject)
session.add_all(subjects)
session.commit()

# Створення оцінок для кожного студента з усіх предметів
for student in students:
    for subject in subjects:
        for _ in range(randint(10, 20)):
            grade = Grade(value=randint(1, 12), date_received=fake.date_time_between(start_date='-1y', end_date='now'), student=student, subject=subject)
            print(grade)
            session.add(grade)
session.commit()