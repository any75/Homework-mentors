class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def to_lector_grade(self, course, lector, grade):
        if course in self.courses_in_progress and isinstance(lector, Lector) and course in lector.courses_attached:
           if course in lector.from_student_grade:
               lector.from_student_grade[course].append(grade)
           else:
               lector.from_student_grade[course]=[grade]
        else:
            print("Error")

    def __str__(self):
        count = 0
        total = 0
        for i in self.grades:
            count += len(self.grades[i])
            total += sum(self.grades[i])
        if count > 0:
            average = round(total / count, 1)
        else:
            average = "Оценок нет"
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\
        \nЗавершенные курсы: {', '.join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'
class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.from_student_grade = {}
    def __str__(self):
        count = 0
        total = 0
        for i in self.from_student_grade:
            count += len(self.from_student_grade[i])
            total += sum(self.from_student_grade[i])
        if count > 0:
            average = round(total / count, 1)
        else:
            average = "Оценок нет"
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average}'
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def to_student_grade(self, course, student, grade):
        if course in self.courses_attached and isinstance(student, Student) and course in student.courses_in_progress:
           if course in student.grades:
               student.grades[course].append(grade)
           else:
               student.grades[course]=[grade]
        else:
            print("Error")




best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.add_courses('Введение в программирование')
print(best_student)
lector1 = Lector(name = 'Some', surname = 'Buddy')
lector1.courses_attached += ['Python']
best_student.to_lector_grade('Python', lector1, 10)
print(lector1.from_student_grade)
print()
print(lector1)
reviewer1 = Reviewer ('Any', 'Smith')
reviewer1.courses_attached += ['Python']
reviewer1.to_student_grade('Python', best_student, 10)
reviewer1.to_student_grade('Python', best_student, 6)
print(best_student)
print(best_student.grades)
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)