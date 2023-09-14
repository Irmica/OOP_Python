import PersonClasses as pc
import Services as sc
import CreatePerson as cp
# Создание групп студентов
asou_1 = pc.StudentGroup()
asou_1.add_member(cp.student_1)
asou_1.add_member(cp.student_2)
asou_1.add_member(cp.student_3)
asou_1.add_member(cp.student_4)
asou_1.add_member(cp.student_5)
asou_1.add_member(cp.student_6)
asou_1.add_member(cp.student_7)

asou_2 = pc.StudentGroup()
asou_2.add_member(cp.student_29)
asou_2.add_member(cp.student_30)
asou_2.add_member(cp.student_31)
asou_2.add_member(cp.student_32)
asou_2.add_member(cp.student_33)

asou_3 = pc.StudentGroup()
asou_3.add_member(cp.student_8)
asou_3.add_member(cp.student_9)
asou_3.add_member(cp.student_10)
asou_3.add_member(cp.student_11)
asou_3.add_member(cp.student_12)
asou_3.add_member(cp.student_13)
asou_3.add_member(cp.student_14)
asou_3.add_member(cp.student_15)

asou_4 = pc.StudentGroup()
asou_4.add_member(cp.student_16)
asou_4.add_member(cp.student_17)
asou_4.add_member(cp.student_18)
asou_4.add_member(cp.student_19)
asou_4.add_member(cp.student_20)

asou_5 = pc.StudentGroup()
asou_5.add_member(cp.student_21)
asou_5.add_member(cp.student_22)
asou_5.add_member(cp.student_23)
asou_5.add_member(cp.student_24)
asou_5.add_member(cp.student_25)
asou_5.add_member(cp.student_26)
asou_5.add_member(cp.student_27)
asou_5.add_member(cp.student_28)
# Создание потоков
stream_1 = pc.StudentStream()
stream_1.add_group_to_stream(asou_1)
stream_1.add_group_to_stream(asou_2)

stream_2 = pc.StudentStream()
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
# Вывод в консоль списка студентов в каждой группе в каждом потоке
stream_1.output_to_the_console()
stream_2.output_to_the_console()
# Сортировка и вывод в консоль 2 потока
print("Отсортированный 2 поток:")
stream_2.sort_stream_by_number_of_students()
stream_2.output_to_the_console()
