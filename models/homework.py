class Homework:
    def __init__(self, score,):
        self.score = score
        
    def __add__(self, other):
        self.balance += other.balance
        
    def __str__(self):
        return f""