from analyzer import Analyser

analyze = Analyser()
class  StudentAnalyzer:
    
    def __init__(self):
        pass
    
    
    def input_func(self):
        with open('students.txt','r',errors='ignore') as file:
            contents = file.readlines()
            print(contents)
            names = []
            marks = []
            for i in contents:
                temp = ''.join(i).replace('\n','').split('=')
            
                # for i in temp:
                #     if i.isdigit(): 
                #         marks.append(i)
                analyze.studentsnames = temp[0]
                analyze.students()
                
                print(analyze.studentsnames)
                
                avg = 0
                for name in analyze.studentsnames:
                    analyze.studentsmarks = temp[1]
                    analyze.marks()

                        
                    print(analyze.intstumarks)
                print(analyze.intstumarks)

                counter = 0
                for names in analyze.studentsnames:
                    
                    analyze.displayer[names] = analyze.intstumarks[counter]
                    counter +=1
                print(analyze.display)
                
        # with open('Performance_Analyser.txt','w', errors='ignore')

    input_func(self=None)
                

    
    
    