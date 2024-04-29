class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def to_lector_grade(self, course, lector, grade):
        if course in self.courses_in_progress and isinstance(lector, Lector) and course in lector.courses_attached:
           if course in lector.from_student_grade:
               lector.from_student_grade[course].append(grade)
           else:
               lector.from_student_grade[course]=[grade]
           lector.average_grade = lector.average_method()
        else:
            print("Error")
    def average_method(self):
        count = 0
        total = 0
        for i in self.grades:
            count += len(self.grades[i])
            total += sum(self.grades[i])
        result = round(total / count, 1)
        return result

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\
        \nЗавершенные курсы: {", ".join(self.finished_courses)}'
    def __gt__(self, other):
        if isinstance(other, Student):
           result = self.average_grade > other.average_grade
        else:
            result = f'не является студентом'
        return result
    def __ge__(self, other):
        if isinstance(other, Student):
            result = self.average_grade >= other.average_grade
        else:
            result = f'не является студентом'
        return result
    def __le__(self, other):
        if isinstance(other, Student):
            result = self.average_grade <= other.average_grade
        else:
            result = f'не является студентом'
        return result
    def __lt__(self, other):
        if isinstance(other, Student):
            result = self.average_grade < other.average_grade
        else:
            result = f'не является студентом'
        return result
    def __eq__(self, other):
        if isinstance(other, Student):
            result = self.average_grade == other.average_grade
        else:
            result = f'не является студентом'
        return result
    def __ne__(self, other):
        if isinstance(other, Student):
            result = self.average_grade != other.average_grade
        else:
            result = f'не является студентом'
        return result

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
        self.average_grade = 0
    def average_method(self):
        count = 0
        total = 0
        for i in self.from_student_grade:
            count += len(self.from_student_grade[i])
            total += sum(self.from_student_grade[i])
        result = round(total / count, 1)
        return result
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}'
    def __ge__(self, other):
        if isinstance(other, Lector):
            result = self.average_grade >= other.average_grade
        else:
            result = f'не является лектором'
        return result
    def __gt__(self, other):
        if isinstance(other, Lector):
            result = self.average_grade > other.average_grade
        else:
            result = f'не является лектором'
        return result
    def __le__(self, other):
        if isinstance(other, Lector):
            result = self.average_grade <= other.average_grade
        else:
            result = f'не является лектором'
        return result
    def __lt__(self, other):
        if isinstance(other, Lector):
            result = self.average_grade < other.average_grade
        else:
            result = f'не является лектором'
        return result
    def __eq__(self, other):
        if isinstance(other, Lector):
            result = self.average_grade == other.average_grade
        else:
            result = f'не является лектором'
        return result
    def __ne__(self, other):
        if isinstance(other, Lector):
            result = self.average_grade != other.average_grade
        else:
            result = f'не является лектором'
        return result

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def to_student_grade(self, course, student, grade):
        if course in self.courses_attached and isinstance(student, Student) and course in student.courses_in_progress:
           if course in student.grades:
               student.grades[course].append(grade)
           else:
               student.grades[course]=[grade]
           student.average_grade = student.average_method()
        else:
            print("Error")
def average_grade_students(list_students, course):
    count = 0
    total = 0
    for s in list_students:
        if isinstance(s, Student):
            for key in s.grades:
                if key == course:
                    total += sum(s.grades[key]) / len(s.grades[key])
                    count += 1
            if count == 0:
                result = "Оценок нет"
            else:
                result = round(total / count, 1)
                # print(result)
        else:
            print('Не является студентом')
    if count > 0:
        print(result)
    else:
        print("Недостаточно данных")

        def average_grade_students(list_students, course):
            count = 0
            total = 0
            for s in list_students:
                if isinstance(s, Student):
                    for key in s.grades:
                        if key == course:
                            total += sum(s.grades[key]) / len(s.grades[key])
                            count += 1
                    if count == 0:
                        result = "Оценок нет"
                    else:
                        result = round(total / count, 1)
                        # print(result)
                else:
                    print('Не является студентом')
            if count > 0:
                print(result)
            else:
                print("Недостаточно данных")
def average_grade_lectors(list_lectors, course):
    count = 0
    total = 0
    for l in list_lectors:
        if isinstance(l, Lector):
            for key in l.from_student_grade:
                if key == course:
                    total += sum(l.from_student_grade[key]) / len(l.from_student_grade[key])
                    count += 1
            if count == 0:
                result = "Оценок нет"
            else:
                result = round(total / count, 1)
                # print(result)
        else:
            print('Не является лектором')
    if count > 0:
        print(result)
    else:
        print("Недостаточно данных")





best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student1 = Student('James', 'Show', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student1.courses_in_progress += ['Python']
best_student.add_courses('Введение в программирование')
# print(best_student)
lector1 = Lector(name = 'Some', surname = 'Buddy')
lector = Lector(name = 'Any', surname = 'Makler')
lector1.courses_attached += ['Python']
lector.courses_attached += ['Python']
best_student.to_lector_grade('Python', lector1, 10)
best_student1.to_lector_grade('Python', lector1, 6)
# print(lector1.from_student_grade)
# print()
best_student.to_lector_grade('Python', lector1, 7)
# print(lector1)
reviewer1 = Reviewer ('Any', 'Smith')
reviewer1.courses_attached += ['Python']
reviewer1.to_student_grade('Python', best_student, 10)
reviewer1.to_student_grade('Python', best_student, 6)
# print(best_student)
# print(best_student.grades)
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)
print(best_student >= best_student1)
students = [best_student, best_student1]
lectors = [lector, lector1]
average_grade_students(lectors, 'Python')
average_grade_lectors(lectors, 'Python')
