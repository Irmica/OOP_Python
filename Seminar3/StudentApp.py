import PersonClasses as pc
import Processing as pr
import CreatedPerson as cp
import Services as sc
# Вывод в консоль количества студентов в каждой группе
print(
    f"В группе {cp.asou_1.get_number_of_group()} - {cp.asou_1.get_size_of_group()} студентов")
print(
    f"В группе {cp.asou_2.get_number_of_group()} - {cp.asou_2.get_size_of_group()} студентов")
print(
    f"В группе {cp.asou_3.get_number_of_group()} - {cp.asou_3.get_size_of_group()} студентов")
print(
    f"В группе {cp.asou_4.get_number_of_group()} - {cp.asou_4.get_size_of_group()} студентов")
print(
    f"В группе {cp.asou_5.get_number_of_group()} - {cp.asou_5.get_size_of_group()} студентов")
print('\n')
# Вывод в консоль количества групп в каждом потоке
print(
    f"В потоке {cp.stream_1.get_number_of_stream()} - {cp.stream_1.get_size_of_stream()} группы")
print(
    f"В потоке {cp.stream_2.get_number_of_stream()} - {cp.stream_2.get_size_of_stream()} группы")
print('\n')
# Вывод в консоль списка студентов в каждой группе в каждом потоке
cp.stream_1.output_to_the_console()
cp.stream_2.output_to_the_console()
# Сортировка и вывод в консоль 2 потока
print("Отсортированный 2 поток:")
cp.stream_2.sort_stream_by_number_of_students()
cp.stream_2.output_to_the_console()

student_35 = sc.StudentService.create_student("Синицын", 24) # Создание нового студента
sc.StudentService.add_student_to_all_list(cp.all_students, student_35) # Добавление студента в общий лист

sc.StudentService.output_to_the_console_of_all_students(cp.all_students) # Вывод на консоль всех студентов

print(f"Средний возраст всех студентов {sc.AccountController.averege_age_student(cp.all_students)}")
print(f"Средний возраст всех учителей {sc.AccountController.averege_age_student(cp.all_teachers)}")
print(f"Средний возраст всех сотрудников {sc.AccountController.averege_age_student(cp.all_employees)}")