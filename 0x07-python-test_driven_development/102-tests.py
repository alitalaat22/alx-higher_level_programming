
from ast import alias


class emp:
    def __init__(self, name, age, salary, job_tittle):
        self.name = name
        self.age = age
        self.salary = salary
        self.job_tittle = job_tittle
    
    def targ(self, piece):
        salary_piece = 15
        pieces = salary_piece * piece
        total_value = salary_piece * piece
        target = self.salary + total_value
        print("Total salary = ",target)
        print("salary of pieces = ",{pieces})
    
    def prin(self):
        
        self.name = input("   name    = ")
        self.age = int(input("   age    = "))
        self.salary = float(input("  salary   = "))
        self.job_tittle = input("job tittle = ")
        piece = int(input("how many pice is done: ="))


        print("   name    = ",self.name)
        print("   age     = ", self.age)
        print("  salary   = ",self.salary)
        print("job tittle = ",self.job_tittle)
        print("  target   =",piece)
        self.targ(piece)
em = emp("", 0, 0.0, "",)
em.prin()
