from sqlalchemy import func, desc, and_
from connect_db import session
from models import Student, Grade, Group, Subject, Teacher

# Створюємо запити ORM SQLAlchemy
def select_1():
    students_avg_scores = (session.query(Student.name, func.round(func.avg(Grade.value), 2).label('average_grade')) \
              .select_from(Grade).join(Student).group_by(Student.id)
              .order_by(desc('average_grade')).limit(5).all())

    return students_avg_scores

def select_2(subject_name):
    student = (session.query(Student).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student)
              .order_by(func.avg(Grade.value).desc()).first())
    return student

def select_3(subject_name):
    group_avg_score = (session.query(func.avg(Grade.value)).join(Subject).filter(Subject.name == subject_name).scalar())
    return group_avg_score

def select_4():
    overall_avg_score = session.query(func.avg(Grade.value).label('avg_score')).scalar()
    return overall_avg_score

def select_5(teacher_name):
    teacher_courses = (session.query(Subject.name).join(Teacher).filter(Teacher.name == teacher_name).all())
    return teacher_courses

def select_6(group_name):
    group_students = session.query(Student.name).join(Group).filter(Group.name == group_name).all()
    return group_students

def select_7(group_name, subject_name):
    group_subject_grades = session.query(Student.name, Grade.value).join(Group).join(Grade).join(Subject).filter(Group.name == group_name, Subject.name == subject_name).all()
    return group_subject_grades

def select_8(teacher_name):
    teacher_avg_scores = session.query(func.avg(Grade.value).label('avg_score')).join(Subject).join(Teacher).filter(Teacher.name == teacher_name).scalar()
    return teacher_avg_scores

def select_9(student_name):
    student_courses = (session.query(Subject.name).join(Grade).join(Student).filter(Student.name == student_name).distinct().all())
    return student_courses

def select_10(teacher_id, student_id):
    student_teacher_courses = (session.query(Teacher.name, Student.name, Subject.name) \
              .select_from(Subject).join(Teacher).join(Grade).join(Student)
              .filter(and_(Teacher.id == teacher_id,
                           Student.id == student_id)).group_by(Subject.name, Teacher.name, Student.name)
              .order_by(Subject.name).all())
    return student_teacher_courses


def main():
       
    # Використання функції select_1
    print("Знайти 5 студентів із найбільшим середнім балом з усіх предметів:")
    for student in select_1():
        print(student[0])

    # Використання функції select_2
    print("\nЗнайти студента із найвищим середнім балом з певного предмета:")
    print(select_2("Fully-configurable clear-thinking benchmark"))

    # Використання функції select_3
    print("\nЗнайти середній бал у групах з певного предмета:")
    for avg_grade in select_3("Fully-configurable clear-thinking benchmark"):
        print(avg_grade[0])

    # Використання функції select_4
    print("\nЗнайти середній бал на потоці (по всій таблиці оцінок):")
    avg_grade_overall = select_4()
    print(avg_grade_overall)

    # Використання функції select_5
    print("\nЗнайти які курси читає певний викладач:")
    courses_taught_by_teacher = select_5("Megan Brown")
    for course in courses_taught_by_teacher:
        print(course.name)

    # Використання функції select_6
    print("\nЗнайти список студентів у певній групі:")
    students_in_group = select_6("Group 3")
    for student in students_in_group:
        print(student.name)

    # Використання функції select_7
    print("\nЗнайти оцінки студентів у окремій групі з певного предмета:")
    grades_in_group = select_7("Group 3", "Quality-focused client-driven Graphic Interface")
    for grade in grades_in_group:
        print(grade.value)

    # Використання функції select_8
    print("\nЗнайти середній бал, який ставить певний викладач зі своїх предметів:")
    avg_grade_by_teacher = select_8("Megan Brown")
    print(avg_grade_by_teacher)

    # Використання функції select_9
    print("\nЗнайти список курсів, які відвідує певний студент:")
    courses_attended_by_student = select_9("Gina Smith")
    for course in courses_attended_by_student:
        print(course.name)

    # Використання функції select_10
    print("\nСписок курсів, які певному студенту читає певний викладач:")
    courses_taught_to_student_by_teacher = select_10("Gina Smith", "Megan Brown")
    for course in select_10(8, 51):
        print(course)

if __name__ == "__main__":
    main()

