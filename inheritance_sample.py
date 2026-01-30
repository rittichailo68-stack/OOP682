class Person:
    def __init__(self, id, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, pid, name, age, student_id):
        super().__init__(pid, name, age)
        self.staff_id = student_id

class Staff(Person):
    def __init__(self, pid, name, age, staff_id):
        super().__init__(pid, name, age)
        self.staff_id = staff_id

student = Student(123456789023, "Alice", 20, "S123")
staff = Staff(1234567890123, "Bob", 35, "ST2001")


def get_person_info(person):
    print(isinstance(person, Person))
    return f"Name: {person.name}, Age{person.age}"