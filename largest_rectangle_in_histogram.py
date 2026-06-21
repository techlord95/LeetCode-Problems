from typing import List 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        # Heights in the stack are monotonically increasing
        # Each bar “waits” until a smaller bar appears to compute its max rectangle
        
        for i , h in enumerate(heights): # Assume current bar starts at i
            index_start = i 
            
            #non empty stack , top element grater than the height
            while stack and stack[-1][1] > h :
                index , height = stack.pop() # popping higher bars 
                # if curr height h is smaller , prev taller bars can't extend further
                maxArea = max(maxArea , height *(i-index)) 
                
                index_start = index 
                
            stack.append((index_start ,h))
            
        # cleanup  reamining bars that never found a smaller element 
        for i, h in stack:
            maxArea = max(maxArea , h *(len(heights) -i ))
        return maxArea
     

#solution uses monotonic increasing stack    
     
# Time: O(n) (each element pushed & popped once)

# Space: O(n) (stack)   

# Each bar stays in the stack until a smaller bar forces it to compute its maximum possible rectangle.