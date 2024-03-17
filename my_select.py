from sqlalchemy import func
from connect_db import session
from models import Student, Grade, Group, Subject, Teacher


def select_1():
    students_avg_scores = session.query(Student, func.avg(Grade.value).label('avg_score')).join(Grade).group_by(Student).order_by(func.avg(Grade.value).desc()).limit(5).all()
    return students_avg_scores

def select_2(subject_name):
    student = session.query(Student).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student).order_by(func.avg(Grade.value).desc()).first()
    return student

def select_3(subject_name):
    group_avg_score = session.query(Group, func.avg(Grade.value).label('avg_score')).join(Student).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Group).all()
    return group_avg_score

def select_4():
    overall_avg_score = session.query(func.avg(Grade.value).label('avg_score')).scalar()
    return overall_avg_score

def select_5(teacher_name):
    teacher_courses = session.query(Subject).join(Teacher).filter(Teacher.name == teacher_name).all()
    return teacher_courses

def select_6(group_name):
    group_students = session.query(Student).join(Group).filter(Group.name == group_name).all()
    return group_students

def select_7(group_name, subject_name):
    group_subject_grades = session.query(Student, Grade).join(Group).join(Grade).join(Subject).filter(Group.name == group_name, Subject.name == subject_name).all()
    return group_subject_grades

def select_8(teacher_name):
    teacher_avg_scores = session.query(func.avg(Grade.value).label('avg_score')).join(Subject).join(Teacher).filter(Teacher.name == teacher_name).scalar()
    return teacher_avg_scores

def select_9(student_name):
    student_courses = session.query(Subject).join(Grade).join(Student).filter(Student.name == student_name).all()
    return student_courses

def select_10(student_name, teacher_name):
    student_teacher_courses = session.query(Subject).join(Grade).join(Student).join(Teacher).filter(Student.name == student_name, Teacher.name == teacher_name).all()
    return student_teacher_courses


def main():
       
    # Використання функції select_1
    print("Знайти 5 студентів із найбільшим середнім балом з усіх предметів:")
    students_with_highest_avg_grades = select_1()
    for student in students_with_highest_avg_grades:
        print(student.name)

    # Використання функції select_2
    print("\nЗнайти студента із найвищим середнім балом з певного предмета:")
    highest_avg_grade_student = select_2("Quality-focused client-driven Graphic Interface")
    print(highest_avg_grade_student.name)

    # Використання функції select_3
    print("\nЗнайти середній бал у групах з певного предмета:")
    avg_grades_by_group = select_3("Quality-focused client-driven Graphic Interface")
    for avg_grade in avg_grades_by_group:
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
    for course in courses_taught_to_student_by_teacher:
        print(course.name)

if __name__ == "__main__":
    main()

