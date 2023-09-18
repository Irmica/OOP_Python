import PersonClasses as pc
"""Модуль с классами обработки (вывод в консоль потоков, сортировка групп в потоке по количеству студентов в них)"""


class Iterable:
    """Класс для вывода списков студентов потока в консоль"""
    @staticmethod
    def out(stream: list) -> None:
        print(f"Список студентов {stream[0]} потока.")
        for i in range(1, len(stream)):
            print(
                f"Список группы {pc.StudentGroup.get_number_of_group(stream[i])}:")
            for j in range(1, pc.StudentGroup.get_size_of_group(stream[i]) + 1):
                member = pc.StudentGroup.get_member_by_index(stream[i], j)
                name = pc.Student.get_name(member)
                print(f"{j}. {name}")


class Sorting:
    """Класс для сортировки потока по количеству студентов в группе.
    Сортировка по возрастанию. Метод сортировки - сортировка выбором"""
    @staticmethod
    def sort_group_by_members(stream: list):
        for i in range(1, len(stream) - 1):
            min_idx = i
            for idx in range(i + 1, len(stream) - 1):
                if pc.StudentGroup.get_size_of_group(stream[idx]) < pc.StudentGroup.get_size_of_group(stream[min_idx]):
                    min_idx = idx
            stream[i], stream[min_idx] = stream[min_idx], stream[i]
        return stream
