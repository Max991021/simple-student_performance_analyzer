from analyzer import Analyser

analyze = Analyser()
class  StudentAnalyzer:
    
    def __init__(self):
        pass
    
    
    def input_func(self):
        with open('students.txt','r',errors='ignore') as file:
            contents = file.readlines()
            print(contents)
            counter = 0
            for i in contents:
                temp = ''.join(i).replace('\n','').split('=')

                analyze.studentsnames = temp[0]
                analyze.students()
            
                
               
                analyze.studentsmarks = temp[1]
                analyze.marks()
                
                

                        
                
                print(analyze.studentsnames)

                
                for names in analyze.studentsnames:
                    
                    analyze.displayer[names] = analyze.intstumarks[counter]
                    counter +=1
                    
                print(analyze.intstumarks)
                print(analyze.display)
            #print(analyze.avg())
                
        # with open('Performance_Analyser.txt','w', errors='ignore') as file:
        #     file.write('-----------------This Is The Student Performance Analyser------------------------')
            
        analyze.displayer

    input_func(self=None)
                

    
    
    