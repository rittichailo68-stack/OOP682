class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.student = []
    
    def add_student(self, student):
        self.student.append(student)

    def __len__(self):
        return len(self.students)
    
    def __getitem__ (self, index):
        return self.students[index]
        
