import math

class Analyser:
    
    def __init__(self,studentsmarks = None,avarage = None,studentsnames = None,displayer = None):
        self.studentsmarks = studentsmarks
        self.avarage = avarage
        self.studentsnames = studentsnames
        self.displayer = displayer
        self.intstumarks = []
        
    def students(self):
        self.studentsnames = self.studentsnames.split(',')
        
        return self.studentsnames
    
    def marks(self, ):
        
        
        self.studentsmarks = self.studentsmarks.split(',')
        marks = []
        for elements in self.studentsmarks:
            
            elements = int(elements)
            marks.append(elements)
                
        marks.append(sum(marks)/len(marks))
        self.intstumarks.append(marks)
        
        # for names in self.studentsnames:
        #     for i in self.intstumarks:
        #         self.displayer[names] = self.intstumarks[i]
        # print(self.studentsmarks)

        return self.intstumarks
    
    def avg(self):
        
        self.avarage = sum(self.intstumarks)/len(self.intstumarks)
        
        return self.avarage
        
    @property
    def display(self):
        sorted_items = self.displayer.sorted(self.displayer.items(), key=lambda: sum(item[1]), reverse = True)
        
        return f'This is the list of the students that have performed from highest to lowest: {sorted_items}'
        
        

            