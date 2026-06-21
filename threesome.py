from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result_in_list = []
        
        nums.sort() # O(nlogn) helps to skip duplicates easily # it uses timsort 
        
        # for iteration using enumerate
        # i is the index value and a is the current value of the element
        
        for i , a in enumerate(nums): # if a is same as the previous element then skip it 
            if i > 0 and a == nums[i-1]:
                continue 
        
        # starting at i + 1 as we already have found one element at a , 2 more are required     
            left_ptr , right_ptr = i+1  , len(nums) - 1
        
           # adding nums of 3 some 
            while left_ptr < right_ptr:
                threesome = a + nums[left_ptr] + nums[right_ptr]
                # timsort sorts in ascending order ,decrement right to get smaller value
                if threesome > 0:
                    right_ptr -=1
                elif threesome < 0:
                    left_ptr +=1
                else:
                # add the triplets at this point a valid triplet with sum ==0 is found 
                    result_in_list.append([a, nums[left_ptr] , nums[right_ptr]])
                #moving left_ptr forward since that number is already used , don't use same element immediately 
                    left_ptr +=1
                
                # if we don't skip , same triplet can be formed again , while keeps moving left_ptr forward until it lands on a unique number 
                    while nums[left_ptr] == nums[left_ptr - 1] and left_ptr < right_ptr:
                        left_ptr +=1 
        return result_in_list
    
#  time = O(n^2)
#  space = O(1)
                    
# TIME COMPLEXITY
   
# Sorting: O(n log n)

# Outer loop: O(n)

# Two pointers per element: O(n)

# Total: O(n²)  (optimal for this problem)

# SPACE

# Sorting → in-place, so O(1) extra space.

# Pointers and temporary variables → constant space.

# Result list → stores all valid triplets.

# Worst case: if all numbers are 0, you can have ~O(n²) triplets.

# So result storage: O(k), where k = number of solutions.

#  Space: O(1) auxiliary, plus O(k) for the output.

# TOTAL O(1) + O(k)

# k is the number of valid triplets 

# The Python enumerate() function is a built-in tool that allows you to loop over an iterable (like a list, tuple, or string) 
# while keeping track of the current item's index. It eliminates the need for manual counter variables

# for i, a in enumerate(nums):
# i → index
# a → value at that index (nums[i])
# You iterate through the array, typically after sorting it.

# Sorting is critical because it allows:

# Duplicate detection
# Two-pointer technique later
# ⛔ Duplicate Skipping Logic
# if i > 0 and a == nums[i-1]:
#     continue

# This is the key optimization.

# What it does:
# It skips duplicate values of a (the first element of the triplet).
# Ensures you don’t generate the same triplet multiple times.
