from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() #index storing 
        
        left_pointer = right_pointer = 0 
        
        while right_pointer < len(nums):
            # while q is non empty , pop smaller values from queue ,q[-1] is the rightmost value
            while q and nums[q[-1]] < nums[right_pointer]:
                q.pop()
            q.append(right_pointer)
            
            
            # removing left value from the window
            if left_pointer > q[0]:
                q.popleft()
             
            # edge case to check that our window is at least of size = k    
            if (right_pointer + 1 ) >=k:
                output.append(nums[q[0]]) # for each window appending the maximum output , inside append is not the index but the actual value itself
                left_pointer += 1
            right_pointer +=1
        return output 
        
        
        
        
# Approach

# create a window of k and check for the max element 

# A Monotonic Decreasing Queue  (dequeue) is used in order to choose the elements easily 


# [8,7,6,5]   k= 2

# [8,7] -> 8 
# [7,6] -> 7
# [6,5] -> 6   

# output 

# [8,7,6]