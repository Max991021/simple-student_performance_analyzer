import math

class Analyser:
    
    def __init__(self,studentsmarks = None,avarage = None,studentsnames = None,displayer = None):
        self.studentsmarks = studentsmarks
        self.avarage = avarage
        self.studentsnames = studentsnames
        self.displayer = {}
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
        sorted_items = dict(sorted(self.displayer.items(), key=lambda item: sum(item[1]), reverse = True))
        with open('Performance_Analyser.txt','w', errors='ignore') as file:
            file.write('-----------------This Is The Student Performance Analyser------------------------\n')
            count = 1
            for key,value in sorted_items.items():
                # new = ','.join(str(i) for i in value)
                output = f'No. {count} is {key} with the marks {','.join(str(i) for i in value[:-1])} and the avarage of {str(value[-1])}\n'
                count +=1
                file.write(output)
                
    
        return sorted_items
        

            