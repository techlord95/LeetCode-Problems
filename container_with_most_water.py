class Solution:
    def maxArea(self, height: list[int]) -> int:
        result  = 0 #starting the iteration from 0 
        left_ptr , right_ptr = 0 , len(height) -1  #start till end of the list 
        
        while left_ptr < right_ptr:
            area = (right_ptr-left_ptr) *min(height[left_ptr] , height[right_ptr])  #area of rectangle len x breadth here it is breadth x len where len is min of the height to hold water 
            result = max(result,area) # to keep updating the best answer as we move left to right 
            
            if height[left_ptr] < height[right_ptr]: #moving to the pointer which has lower height/length 
                left_ptr +=1
                
            else:
                right_ptr -=1
        return result
    
    
# Time - O(n)
# Space - O(1)



# area = l x b or height x width 
# height  = 7 x 7(width)



        
                 
        
        
        
        
       
        
        