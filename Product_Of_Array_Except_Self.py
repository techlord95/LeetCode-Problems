# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# TIME COMPLEXITY

# Time: Two single passes → O(n).

# Space: result_arr is required output, so extra space is just prefix_val and postfix_val → O(1) auxiliary.

# Solution 
from typing import List
class Solution:
    def ProductExceptSelf(self, nums:List[int])->list[int]:
        # identity matrix is made [1,1,1,1]
        result_array = [1] * (len(nums))
        
        prefix_value = 1
        # Left to RIght(prefix pass loop) 

        for i in range(len(nums)):
            result_array[i] = prefix_value
            prefix_value *= nums[i] # It contains the product of elements before i
        
        postfix_value = 1 
        # Right to left (postfix pass loop)
        # Range has range(start,stop,step)
        # len(nums) is 4 so range becomes (3,-1,-1)
        
        for i in range(len(nums)-1,-1,-1):
            result_array[i] *= postfix_value # multiply the product of elements right of i  result_array = prefix product x postfix product(product of every element except self) 
            postfix_value *= nums[i]
            
        return result_array
            

# step by step 

# Step 1 -> [1,2,3,4] input 
# Step 2 -> [1,1,1,1] gets converted into identity matrix 

# Step 3 -> goes in loop 
# result_array[i] prefix_value where p_v is 1

# after * multiplication updation


        #   Action
        
# step 0) res_arr[0]=pre_val          1*1 [1,1,1,1]

# step 1) write 1                     1*2 [1,1,1,1]

# step 2) write 2                     2*3 [1,1,2,1]

# step 3)write 6           6*4 used later [1,1,2,6]

# each cell holds product of elements before it 


# Step 4 -> 

      
        #   Action
        # res_arr[i]*=post_val                          postfixt_value *= nums[i]
               
# step 3) 6*1                              [1,1,2,6]         1*4 = 4

# step 2) 2*4                             [1,1,8,6]          4*3 = 12 

# step 1) 1*12                            [1,12,8,6]         12*2 =24 

# step 0) 1*24                            [24,12,8,6]        24*1 = 24



# | Index | Value stored | How it was formed              |
# | ----- | ------------ | ------------------------------ |
# | 0     | 24           | prefix `1`  ×  postfix `2·3·4` |
# | 1     | 12           | prefix `1`  ×  postfix `3·4`   |
# | 2     | 8            | prefix `1·2` ×  postfix `4`    |
# | 3     | 6            | prefix `1·2·3` ×  postfix `1`  |




class Solution(object):
    def productExceptSelf(self, nums):
        #making iden(tity) matrix
        result = [1] * len(nums) 
        prefix_val = 1 
        
        for i in range(len(nums)):
            result[i] = prefix_val
            prefix_val *= nums[i]
            
        postfix_val = 1
        
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix_val
            postfix_val *= nums[i]
        return result
a1 = Solution().productExceptSelf(nums=[1,2,3,4])
print(a1)

