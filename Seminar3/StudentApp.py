class Iterable:
    '''Класс для вывода списков студентов потока в косоль'''

    def out(self, stream: list):
        print(f"Список студентов {stream[0]} потока.")
        for i in range(1, len(stream)):
            print(
                f"Список группы {StudentGroup.get_number_of_group(stream[i])}:")
            for j in range(1, StudentGroup.get_size_of_group(stream[i])+1):
                member = StudentGroup.get_member_by_index(stream[i], j)
                name = Student.get_name(member)
                print(f"{j}. {name}")


class Comparable:
    '''Класс для сортировки потока по количеству студентов в группе. 
    Сортировка по убыванию. Метод сортировки - сортировка выбором'''

    def sort_group_by_members(self, stream):
        for i in range(1, len(stream) - 1):
            min_idx = i
            for idx in range(i + 1, len(stream)-1):
                if StudentGroup.get_size_of_group(stream[idx]) < StudentGroup.get_size_of_group(stream[min_idx]):
                    min_idx = idx
            stream[i], stream[min_idx] = stream[min_idx], stream[i]
        return stream


class Person:
    '''Родительский класс для студентов, учетилей и сотрудников'''

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
    '''Класс студента'''
    ID_STUDENT = 1 # id студента присваивается по порядку

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.id = Student.ID_STUDENT
        Student.ID_STUDENT += 1
# getters and setters

    def get_id(self):
        return self.id


class Teacher(Person):
    '''Клас Учитель, не используется'''

    def __init__(self, name: str, age: int, degree: str) -> None:
        super().__init__(name, age)
        self.degree = degree
# getters and setters

    def get_degree(self):
        return self.degree

    def set_degree(self, new_degree: str):
        self.degree = new_degree


class Employee(Person):
    '''Класс Сотрудник, не используется'''

    def __init__(self, name: str, age: int, specialization: str) -> None:
        super().__init__(name, age)
        self.specialization = specialization
# getters and setters

    def get_specialization(self):
        return self.specialization

    def set_specialization(self, new_specialization: str):
        self.specialization = new_specialization


class StudentGroup:
    '''Класс Студенчесткой группы'''
    NUMBER_OF_GROUP = 1 # Номер группы присваивается по порядку

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
        size = len(self.list_of_students)-1
        return size

    def get_member_by_index(self, index):
        return self.list_of_students[index]


class StudentStream(Iterable, Comparable):
    NUMBER_OF_STREAM = 1 # Номер потока присваивается по порядку

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
        return len(self.stream)-1

    def output_to_the_console(self):
        '''метод вывода на консоль списка студентов по группам'''
        super().out(self.stream)

    def sort_stream_by_number_of_students(self):
        '''метод сортировки потока по количеству студентов в группе'''
        super().sort_group_by_members(self.stream)

# Создание студентов
student_1 = Student("Алексеев", 18)
student_2 = Student("Андреев", 19)
student_3 = Student("Борисова", 20)
student_4 = Student("Воронцова", 20)
student_5 = Student("Галушкина", 21)
student_6 = Student("Гурченкова", 19)
student_7 = Student("Гуторов", 22)
student_8 = Student("Деменкова", 20)
student_9 = Student("Демочкин", 18)
student_10 = Student("Калугин", 18)
student_11 = Student("Киселева", 18)
student_12 = Student("Коротков", 19)
student_13 = Student("Кравчук", 18)
student_14 = Student("Леонтьева", 19)
student_15 = Student("Михальченков", 18)
student_16 = Student("Мухин", 22)
student_17 = Student("Остапенко", 20)
student_18 = Student("Полохова", 19)
student_19 = Student("Путятина", 18)
student_20 = Student("Саврухина", 18)
student_21 = Student("Симонова", 18)
student_22 = Student("Степанов", 19)
student_23 = Student("Усов", 18)
student_24 = Student("Черненкова", 18)
student_25 = Student("Черногузов", 21)
student_26 = Student("Черткова", 12)
student_27 = Student("Чайко", 18)
student_28 = Student("Навальнев", 19)
student_29 = Student("Шептухин", 18)
student_30 = Student("Чипига", 22)
student_31 = Student("Пищухин", 18)
student_32 = Student("Подопригора", 19)
student_33 = Student("Швецов", 18)
# Создание групп студентов
asou_1 = StudentGroup()
asou_1.add_member(student_1)
asou_1.add_member(student_2)
asou_1.add_member(student_3)
asou_1.add_member(student_4)
asou_1.add_member(student_5)
asou_1.add_member(student_6)
asou_1.add_member(student_7)

asou_2 = StudentGroup()
asou_2.add_member(student_29)
asou_2.add_member(student_30)
asou_2.add_member(student_31)
asou_2.add_member(student_32)
asou_2.add_member(student_33)

asou_3 = StudentGroup()
asou_3.add_member(student_8)
asou_3.add_member(student_9)
asou_3.add_member(student_10)
asou_3.add_member(student_11)
asou_3.add_member(student_12)
asou_3.add_member(student_13)
asou_3.add_member(student_14)
asou_3.add_member(student_15)

asou_4 = StudentGroup()
asou_4.add_member(student_16)
asou_4.add_member(student_17)
asou_4.add_member(student_18)
asou_4.add_member(student_19)
asou_4.add_member(student_20)

asou_5 = StudentGroup()
asou_5.add_member(student_21)
asou_5.add_member(student_22)
asou_5.add_member(student_23)
asou_5.add_member(student_24)
asou_5.add_member(student_25)
asou_5.add_member(student_26)
asou_5.add_member(student_27)
asou_5.add_member(student_28)
# Создание потоков
stream_1 = StudentStream()
stream_1.add_group_to_stream(asou_1)
stream_1.add_group_to_stream(asou_2)

stream_2 = StudentStream()
stream_2.add_group_to_stream(asou_3)
stream_2.add_group_to_stream(asou_4)
stream_2.add_group_to_stream(asou_5)

# Вывод в консоль количества студентов в каждой группе
print(
    f"В группе {asou_1.get_number_of_group()} - {asou_1.get_size_of_group()} студентов")
print(
    f"В группе {asou_2.get_number_of_group()} - {asou_2.get_size_of_group()} студентов")
print(
    f"В группе {asou_3.get_number_of_group()} - {asou_3.get_size_of_group()} студентов")
print(
    f"В группе {asou_4.get_number_of_group()} - {asou_4.get_size_of_group()} студентов")
print(
    f"В группе {asou_5.get_number_of_group()} - {asou_5.get_size_of_group()} студентов")
print('\n')
# Вывод в консоль количества групп в каждом потоке
print(
    f"В потоке {stream_1.get_number_of_stream()} - {stream_1.get_size_of_stream()} группы")
print(
    f"В потоке {stream_2.get_number_of_stream()} - {stream_2.get_size_of_stream()} группы")
print('\n')
# Вывод в консоль списка студенто в каждой группе в каждом потоке
stream_1.output_to_the_console()
stream_2.output_to_the_console()
# Сортировка и вывод в консоль 2 потока
print("Отсортированный 2 поток")
stream_2.sort_stream_by_number_of_students()
stream_2.output_to_the_console()
