import random
import string

class Person:
    def __init__(self, name, surname, age, address, city, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.city = city
        self.gender = gender

    def display(self):
        print(f'Osoba: {self.name} {self.surname}')
        print(f'Wiek: {self.age}')
        print(f'Adres: {self.address} {self.city}')
        print(f'Plec: {self.gender}')

class Student(Person):
    def __init__(self, name, surname, age, address, city, gender, school_level):
        super().__init__(name, surname, age, address, city, gender)
        self.school_level = school_level

    def display(self):
        super().display()
        print(f'Poziom edukacji: {self.school_level}')

class Teacher(Person):
    def __init__(self, name, surname, age,  address, city, gender, spec):
        super().__init__(name, surname, age, address, city, gender)
        self.spec = spec

    def display(self):
        super().display()
        print(f'Specjalizacja: {self.spec}')

class School:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f'Nazwa Szkoly: {self.name}')

class PrimarySchool(School):
    def __init__(self, name):
        super().__init__(name)
        self.student_id = random.randint(1, 420)

    def display(self):
        super().display()
        print(f'Id: {self.student_id}')
        print(f'Poziom {PrimarySchool.__name__}')

class SecondarySchool(School):
    def __init__(self, name):
        super().__init__(name)
        self.student_id = random.randint(1, 420)

    def display(self):
        super().display()
        print(f'Id: {self.student_id}')
        print(f'Poziom {SecondarySchool.__name__}')

class HighSchool(School):
    def __init__(self, name):
        super().__init__(name)
        self.student_id = random.randint(1, 420)

    def display(self):
        super().display()
        print(f'Id: {self.student_id}')
        print(f'Poziom {HighSchool.__name__}')

class AcademicSchool(School):
    def __init__(self, name):
        super().__init__(name)
        self.student_id = random.randint(1, 420)

    def display(self):
        super().display()
        print(f'Id: {self.student_id}')
        print(f'Poziom {AcademicSchool.__name__}')

def generate_random_person():
    name = random.choice(["John", "Alice", "Bob", "Emma", "David", "Sophia"])
    surname = random.choice(["Smith", "Johnson", "Williams", "Jones", "Brown"])
    age = random.randint(10, 50)
    address = f"{random.randint(100, 999)} {random.choice(string.ascii_uppercase)} Street"
    city = random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"])
    gender = random.choice(["M", "F"])
    return name, surname, age, address, city, gender


def generate_random_student():
    school_level = random.randint(1, 4)
    general_data = generate_random_person()
    return Student(*general_data, school_level)

def generate_random_teacher():
    spec = random.choice(["Math", "Science", "History", "English", "Art"])
    general_data = generate_random_person()
    return Teacher(*general_data, spec)

class SchoolDataset:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def display_students(self):
        print("Lista uczniow:")
        for student in self.students:
            student.display()
            print("\n")

    def display_teachers(self):
        print("Lista nauczycieli:")
        for teacher in self.teachers:
            teacher.display()
            print("\n")


dataset = SchoolDataset()


for _ in range(5):
    dataset.add_student(generate_random_student())

for _ in range(3):
    dataset.add_teacher(generate_random_teacher())


dataset.display_students()
dataset.display_teachers()

class Klasa1(School):


    def Math(self):
