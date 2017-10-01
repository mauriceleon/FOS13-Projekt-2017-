from utility import *
import random
import numpy as np


@maindeco
def main_menue():
    
    
    message_display('Hauptmenü', display_width*0.5, display_width*0.15, 58 )
    
    button( display_width*0.34375, display_height*0.4, display_width*0.3125,display_height/6,'Training', second_menue)
    button( display_width*0.34375, display_height*0.6, display_width*0.3125,display_height/6,'Training', second_menue)



@maindeco
def second_menue():
                   
    button( display_width*0.1, display_height*0.3, display_width*0.3125,display_height/6,'+', add.display_task, size = 60)
    button( display_width*0.55, display_height*0.3, display_width*0.3125,display_height/6,'-',  main_menue, size = 100)
    button( display_width*0.1, display_height*0.5, display_width*0.3125,display_height/6,'*', main_menue, size = 60)
    button( display_width*0.55, display_height*0.5, display_width*0.3125,display_height/6,'/', main_menue, size = 60)

class base_task(object):
    
    size = 50
    Input = label(display_width*0.7, display_height*0.5, size = 40)
    
    def __init__(self,operations, task_num = 10, mixed = False ):
        
        
        self.task_num = task_num
        self.mixed = mixed
        #a list containing operator dict keys
        self.operations = operations
        self.input = label(display_width*0.7, display_height*0.5, size = 40)
        self.record = []
        self.current_task = 0
    
    def generate_numbers(self, start = 0, stop = 20):
        
        self.nums = []
        
        kardinal = len(self.operations) +1
        
        for i in range(kardinal):
            self.nums.append(random.randint(start,stop))
            
        return self.nums
    
    def operation_to_string(self):
                
        self.term = ''.join(str(a) + self.operations[i] for i,a in enumerate(self.nums[:-1])) 
        self.term += str(self.nums[-1]) + ' ='
        return self.term   
        
         
    @maindeco
    def display_task(self):
        
        message_display(self.operation_to_string(),display_width/2,display_height/2, fix_right = 1)
        self.input.fill_values()
        self.input.display()
        button(display_width*0.55, display_height*0.9, display_width*0.3125,display_height/6
               ,'Eingabe', self.enter, size = 50)
   
    def get_result(self):
        raise NotImplementedError        
        new_num = []
        prio_op = []
        low_op = []
        
        for i,operator in enumerate(self.operations):
            
            if operator == '*' or operator == '/':
                prio_op.append(i)
            else:
                low_op.append(i)
                
                
            ergebnis = 0
            zwischenergebnis = 0 
            
            for i,index in enumerate(prio_op):
                
                 if not(i== 0) and (index - prio_op[i-1] == 1):
                     
                     zwichenergebnis = operation[self.operations[index]](zwischenergebnis,self.nums[index+1])                     
                     ergebnis += zwichenergebnis
                     
                 else: 
                     zwichenergebnis = operation[self.operations[index]](self.nums[index],self.nums[index+1])
                     ergebnis += zwichenergebnis
                     
                 try:    
                     if not(index - prio_op[i+1] == -1):
                         new_num.append(ergebnis)
                         ergebnis = 0

                 except:
                        new_num.append(ergebnis)
                        ergebnis = 0
                     
            for i,index in enumerate(low_prio):
                
                ergebnis+=  operation[self.operations[index]](zwischenergebnis,self.nums[index+1])    
             
                     
                     
                     
                     
                
            
        
        if 0:
            ergebnis = 0
            zwischenergebnis = 0
            for i,operator in enumerate(self.operations):
                
                    if not(i == 0) and (self.operations[i-1] == '*' or self.operations[i-1] == '/'):
                        zwischenergebnis = operation[operator](zwischenergebnis,self.nums[i +1])
                        ergebnis +=  zwischenergebnis 
                           
                    else:  
                        zwischenergebnis =  operation[operator](self.nums[i],self.nums[i +1])  
                        ergebnis +=  zwischenergebnis
                    
    
            return ergebnis
                    
                         
    
    def verify(self):
       
       if self.Input.values == self.get_result():
           print('right')
           return 1
       else:
           print('wrong')
           return 0
       
    def enter(self):
        
        self.record.append(self.verify())
        
        if self.current_task < self.task_num:
            self.Input.delete()
            self.generate_numbers()
            self.current_task += 1           
            self.operation_to_string
        else:
            main_menue()
    def init(self):
        
        self.generate_numbers()
        self.operation_to_string()
        
        
add = base_task(['+'])
add.init()     
