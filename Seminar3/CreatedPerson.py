import PersonClasses as pc
"""Модуль для создания экземпляров классов студентов, учетелей и сотрудников"""

# Создание студентов
student_1 = pc.Student("Алексеев", 18)
student_2 = pc.Student("Андреев", 19)
student_3 = pc.Student("Борисова", 20)
student_4 = pc.Student("Воронцова", 20)
student_5 = pc.Student("Галушкина", 21)
student_6 = pc.Student("Гурченкова", 19)
student_7 = pc.Student("Гуторов", 22)
student_8 = pc.Student("Деменкова", 20)
student_9 = pc.Student("Демочкин", 18)
student_10 = pc.Student("Калугин", 18)
student_11 = pc.Student("Киселева", 18)
student_12 = pc.Student("Коротков", 19)
student_13 = pc.Student("Кравчук", 18)
student_14 = pc.Student("Леонтьева", 19)
student_15 = pc.Student("Михальченков", 18)
student_16 = pc.Student("Мухин", 22)
student_17 = pc.Student("Остапенко", 20)
student_18 = pc.Student("Полохова", 19)
student_19 = pc.Student("Путятина", 18)
student_20 = pc.Student("Саврухина", 18)
student_21 = pc.Student("Симонова", 18)
student_22 = pc.Student("Степанов", 19)
student_23 = pc.Student("Усов", 18)
student_24 = pc.Student("Черненкова", 18)
student_25 = pc.Student("Черногузов", 21)
student_26 = pc.Student("Черткова", 12)
student_27 = pc.Student("Чайко", 18)
student_28 = pc.Student("Навальнев", 19)
student_29 = pc.Student("Шептухин", 18)
student_30 = pc.Student("Чипига", 22)
student_31 = pc.Student("Пищухин", 18)
student_32 = pc.Student("Подопригора", 19)
student_33 = pc.Student("Швецов", 18)

# Создание преподавателей

teacher_1 = pc.Teacher("Строев", 52, "Доцент")
teacher_2 = pc.Teacher("Кущевская", 53, "Профессор")
teacher_3 = pc.Teacher("Шульгина", 31, "Аспирант")
teacher_4 = pc.Teacher("Калкаев", 64, "Доцент")
teacher_5 = pc.Teacher("Ложкин", 48, "Доцент")

# Создание сотрудников

employee_1 = pc.Employee("Иванов", 33, "Дворник")
employee_2 = pc.Employee("Петров", 41, "Слесарь")
employee_3 = pc.Employee("Сидоров", 25, "Администратор")
employee_4 = pc.Employee("Смирнов", 39, "Электрик")

# Создание групп студентов
asou_1 = pc.StudentGroup()
asou_1.add_member(student_1)
asou_1.add_member(student_2)
asou_1.add_member(student_3)
asou_1.add_member(student_4)
asou_1.add_member(student_5)
asou_1.add_member(student_6)
asou_1.add_member(student_7)

asou_2 = pc.StudentGroup()
asou_2.add_member(student_29)
asou_2.add_member(student_30)
asou_2.add_member(student_31)
asou_2.add_member(student_32)
asou_2.add_member(student_33)

asou_3 = pc.StudentGroup()
asou_3.add_member(student_8)
asou_3.add_member(student_9)
asou_3.add_member(student_10)
asou_3.add_member(student_11)
asou_3.add_member(student_12)
asou_3.add_member(student_13)
asou_3.add_member(student_14)
asou_3.add_member(student_15)

asou_4 = pc.StudentGroup()
asou_4.add_member(student_16)
asou_4.add_member(student_17)
asou_4.add_member(student_18)
asou_4.add_member(student_19)
asou_4.add_member(student_20)

asou_5 = pc.StudentGroup()
asou_5.add_member(student_21)
asou_5.add_member(student_22)
asou_5.add_member(student_23)
asou_5.add_member(student_24)
asou_5.add_member(student_25)
asou_5.add_member(student_26)
asou_5.add_member(student_27)
asou_5.add_member(student_28)
# Фрмирование общего списка студентов
all_students = []
asou_1.unpack_students(all_students)
asou_2.unpack_students(all_students)
asou_3.unpack_students(all_students)
asou_4.unpack_students(all_students)
asou_5.unpack_students(all_students)

# Создание потоков
stream_1 = pc.StudentStream()
stream_1.add_group_to_stream(asou_1)
stream_1.add_group_to_stream(asou_2)

stream_2 = pc.StudentStream()
stream_2.add_group_to_stream(asou_3)
stream_2.add_group_to_stream(asou_4)
stream_2.add_group_to_stream(asou_5)
# Общий список учителей
all_teachers = []
all_teachers.append(teacher_1)
all_teachers.append(teacher_2)
all_teachers.append(teacher_3)
all_teachers.append(teacher_4)
all_teachers.append(teacher_5)
# Общий список сотрудников
all_employees = []
all_employees.append(employee_1)
all_employees.append(employee_2)
all_employees.append(employee_3)
all_employees.append(employee_4)