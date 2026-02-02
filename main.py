from analyzer import Analyser

analyze = Analyser()
class  StudentAnalyzer:
    
    def __init__(self):
        pass
    
    
    def input_func(self):
        
        analyze.studentsnames = input('Please insert the names of the students to be captured separated by a comma(,): ')
        analyze.students()
        
        for name in analyze.studentsnames:
            analyze.studentsmarks = input(f'Please insert the marks for student {name} saparated by a comma (,):')
            analyze.marks()
            
            
            for elements in analyze.studentsmarks:
                elements = int(elements)
                
                
            
            analyze.studentsmarks.append(analyze.avg())
            
            analyze.displayer[name] = analyze.studentsmarks
            

    input_func(self='')
                

    
    
    