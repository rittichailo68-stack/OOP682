from classroom import ClassRoom
from inheritance_sample import Student


opp = ClassRoom("OOP")
opp.add_student(Student(1, "Alice", 20, "001"))
opp.add_student(Student(2, "Boob", 22, "S002"))
print(f'{opp.name} registered {len(opp)} student')
opp.add_student(Student(3, "Charie", 21, "S003"))
print(len(opp))
print('Student in the class:')
for i in range(len(opp)):
    print(opp[i])
