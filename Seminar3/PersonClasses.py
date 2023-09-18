import Processing as pr
"""Модуль с классами действующих лиц"""


class Person:
    """Родительский класс для студентов, учетелей и сотрудников"""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # getters and setters

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, new_name: str):
        self.name = new_name

    def set_age(self, new_age: int):
        if new_age > 18:
            self.age = new_age


class Student(Person):
    """Класс студента"""
    ID_STUDENT = 1  # id студента присваивается по порядку

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.id = Student.ID_STUDENT
        Student.ID_STUDENT += 1

    # getters and setters

    def get_id(self):
        return self.id

    def output_student(self):
        print(f"ID {self.id} {self.name}")


class Teacher(Person):
    """Клас Учитель"""

    def __init__(self, name: str, age: int, degree: str) -> None:
        super().__init__(name, age)
        self.degree = degree

    # getters and setters

    def get_degree(self):
        return self.degree

    def set_degree(self, new_degree: str):
        self.degree = new_degree


class Employee(Person):
    """Класс Сотрудник"""

    def __init__(self, name: str, age: int, specialization: str) -> None:
        super().__init__(name, age)
        self.specialization = specialization

    # getters and setters

    def get_specialization(self):
        return self.specialization

    def set_specialization(self, new_specialization: str):
        self.specialization = new_specialization


class StudentGroup:
    """Класс Студенческой группы"""
    NUMBER_OF_GROUP = 1  # Номер группы присваивается по порядку

    def __init__(self) -> None:
        self.list_of_students = []
        self.list_of_students.append(StudentGroup.NUMBER_OF_GROUP)
        StudentGroup.NUMBER_OF_GROUP += 1

    # getters and setters
    def get_number_of_group(self):
        return self.list_of_students[0]

    def add_member(self, person: Student):
        self.list_of_students.append(person)

    def get_size_of_group(self):
        size = len(self.list_of_students) - 1
        return size

    def get_member_by_index(self, index): # метод взятия студента по индексу
        return self.list_of_students[index]

    def unpack_students(self, lst: list): # метод распаковки студетов из готовых групп
        lst.extend(self.list_of_students[1:])


class StudentStream(pr.Iterable, pr.Sorting):
    """Класс Студенческого потока"""
    NUMBER_OF_STREAM = 1  # Номер потока присваивается по порядку

    def __init__(self) -> None:
        self.stream = []
        self.stream.append(StudentStream.NUMBER_OF_STREAM)
        StudentStream.NUMBER_OF_STREAM += 1

    # getters and setters
    def get_number_of_stream(self):
        return self.stream[0]

    def add_group_to_stream(self, group: StudentGroup):
        self.stream.append(group)

    def get_size_of_stream(self):
        return len(self.stream) - 1

    def output_to_the_console(self):
        """метод вывода на консоль списка студентов по группам"""
        super().out(self.stream)

    def sort_stream_by_number_of_students(self):
        """метод сортировки потока по количеству студентов в группе"""
        super().sort_group_by_members(self.stream)
