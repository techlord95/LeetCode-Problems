# monotonic stack
# Using a stack that maintains elements in incerasing or decreasing order to efficiently 
# find the next greater element 

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures) # initially result = [0,0,0,0]

        stack = []
        
        # enumerate gives both index and value 
        # i = 0  , temp = 73
        # i = 1  , temp - 74
        for i , temp in enumerate(temperatures):
            # non empty stack check and curr temp is warmer than the top element temp 
            while stack and  temp > stack [-1][0] :
                stack_temp , stack_index = stack.pop() # removing the colder temp
                result[stack_index] = i - stack_index
            stack.append((temp , i ))
        return result
    
    
    
# line 20 , 21 
# stack_temp = 73 , stack_index = 0 , curr index = 1 

# result[stack_index] = i - stack_index becomes result[0] = i - 0 , result[0] = 1 

# which is day 0 had to wait for 1 day to get a warmer temp 