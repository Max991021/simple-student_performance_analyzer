import math

class Analyser:
    
    def __init__(self,studentsmarks,avarage,studentsnames):
        self.studentsmarks = studentsmarks
        self.avarage = avarage
        self.studentsnames = studentsnames
        
        
    def students(self):
        self.studentsnames = self.studentsnames.split(',')
        
        return self.studentsnames
    
    def marks(self):
        self.studentsmarks = []
        
        return self.studentsmarks
    
    def avg(self):
        self.avarage = sum(self.studentsmarks)/len(self.studentsmarks)
        
        return self.avarage
        
    