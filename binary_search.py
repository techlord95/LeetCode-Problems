#iterativve approach , similar to the built-in bisect
from collections import List
class Solution: 
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) -1 
        while left <= right:
            # this approach is used for c++ and java to prevent stack overflow as they have fixed length 
            # mid_element = (left + right) // 2                 # for python can use this 
            
            mid_element = left + ((right-left) //2)
            
            
            # comparing mid value against the target not the index 
            if nums[mid_element] > target :
                right = mid_element -1 
            elif nums[mid_element] < target :
                left = mid_element +1 
            else :
                return mid_element #index value 
        return -1 


# sample arr = [0,1,2,3,4]
# left = 0 ,right = 4 
# formula = left + ((right - left) // 2) -> 0 + (4-0) // 2 -> 2 (the mid element)

# mid_element = (left + right) // 2. can cause stack overflow as in most languages there are fixed integer sizes , 32bit int 
    
# ins = Solution()
# nums = [-1,0,2,4,6,8]
# target = 3
# print(ins.search(nums,target))

# Time = O(log n)
# Space = O(1)


# Built-in function 
#both the solutions have the same time and space , first one is error-prone (<+ bug, return 0 issue)

import bisect 
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        search_ind = bisect.bisect_left(nums,target)

        return search_ind if search_ind < len(nums) and nums[search_ind] ==target else -1

       
        




                
            
        