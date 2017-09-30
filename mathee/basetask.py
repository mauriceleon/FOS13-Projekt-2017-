import random
import numpy as np
from utility import *
from PIL import ImageFont

class base_task(object):
    
    size = 50
    #Input = label()   
    def __init__(self,task_num = 10, difficulty = 0 ):
        
        self.difficulty = difficulty
        self.task_num = task_num
        
    
    def randomtuple(self, start = 0, stop = 20, num = 2):
        
        self.nums = np.array([])
        
        for i in range(num):
            self.nums.append(random.randint(start,stop))
            
        return self.nums
    
    def operation_to_string(self, operator):
        
        try:
            
         self.term = ''.join(str(a) + operator[i] for a,i in enumerate(self.nums[:-1])) + str(self.nums[-1] + '=') 
           
        except:
         self.term = ''.join(str(a) + operator for a in self.nums[:-1]) + str(self.nums[-1] +'=')
    if 0:     
        def compute_position(self):
            #Position für ein fixiertes rechtes Ende
            font = ImageFont.truetype(schrift, self.size)
            size = font.getsize(self.term)    
            pos = (display_width -size[0])/2
            return pos
    
        