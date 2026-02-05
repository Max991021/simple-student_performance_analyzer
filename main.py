from analyzer import Analyser

analyze = Analyser()
class  StudentAnalyzer:
    
    def __init__(self):
        pass
    
    
    def input_func(self):
        
        analyze.studentsnames = input('Please insert the names of the students to be captured separated by a comma(,): ')
        analyze.students()
        
        print(analyze.studentsnames)
        
        avg = 0
        for name in analyze.studentsnames:
            analyze.studentsmarks = input(f'Please insert the marks for student {name} saparated by a comma (,):')
            analyze.marks()

                
            print(analyze.intstumarks)
        print(analyze.intstumarks)
        # for elements in analyze.studentsmarks:
        #     elements = int(elements)
        #     analyze.intstumarks.append(elements)
            
                
            
        #     analyze.intstumarks.append(analyze.avg())
        #     print(analyze.studentsmarks)
        # for name in analyze.intstumarks:
        #     analyze.displayer[name] = analyze.intstumarks
        

        for names in analyze.studentsnames:
            for i in analyze.intstumarks:
                analyze.displayer[names] = analyze.intstumarks[i]
        print(analyze.display)
            

    input_func(self=None)
                

    
    
    