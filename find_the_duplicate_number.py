# Floyd's Tortoise and Hare Algorithm

from typing import List

# use of slow and fast pointers 
class Solution:
    def findDuplicate(self,nums:List[int]) -> int:
        slow_ptr , fast_ptr = 0 , 0 
        
        while True:
            # here we break till the pointers meet at some point 
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[nums[fast_ptr]]
            if slow_ptr == fast_ptr:
                break 
            # this does not mean duplicate is found 
        
        slow_ptr2 = 0 
        while True:
            # slow is currently inside the cycle
            # slow2 starts before the cycle

            slow_ptr = nums[slow_ptr]
            slow_ptr2= nums[slow_ptr2]
            
            # here Because of Floyd's cycle math, when both move one step, they meet exactly at the cycle entrance
            if slow_ptr == slow_ptr2:
                return slow_ptr
            











#brute force sorting using tim sort 
# class Solution:
#     def findDuplicate(self,nums:List[int]) -> int:
#         nums.sort()
#         for i in range(len(nums) -1 ):
#             if nums[i] == nums[i+1]:
#                 return nums[i]
#         return -1 
    
    
# Time -> O(nlogn) 
# Space-> O(n) # requires extra space for worst case 
        
        