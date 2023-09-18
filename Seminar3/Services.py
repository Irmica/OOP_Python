import PersonClasses as pc


class PersonService(pc.Person):
    def create_person(self, name: str, age: int):
        super().__init__(name, age)

    def read_person(self):
        pass

    def update_person(self):
        pass

    def delete_person(self):
        pass


class StudentService(PersonService):
    @staticmethod
    def create_student(name: str, age: int):
        std = pc.Student(name, age)
        return std

    @staticmethod
    def add_student_to_all_list(lst: list, student: pc.Student):
        lst.append(student)
        
    @staticmethod
    def output_to_the_console_of_all_students(lst: list):
        for i in range(0, len(lst)):
            pc.Student.output_student(lst[i])

class AccountController: 
    """Класс для вычисления среднего возраста студентов, учителей и сотрудников"""
    @staticmethod
    def averege_age_student(lst: list):
        sum = 0
        for std in lst:
            sum += pc.Person.get_age(std)
        return sum/len(lst)    

class TeacherService(PersonService, pc.Teacher):
    def create_teacher(self, name: str, age: int, degree: str):
        super().__init__(name, age, degree)


class Employee(PersonService, pc.Employee):
    def create_employee(self, name: str, age: int, specialization: str):
        super().__init__(name, age, specialization)




