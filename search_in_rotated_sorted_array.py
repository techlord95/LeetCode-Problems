# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
        
#         # Initialize left and right pointers for the binary search window
#         left , right = 0 , len(nums) -1 
        
#         # Perform binary search
#         while left <=right :
#             # Calculate the middle element
#             mid_element = (left+right) //2 
            
#             # If target is found at mid, return its index
#             if target == nums[mid_element]:
#                 return mid_element
            
#             # Check if the left half is sorted
#             if nums[left] <= nums[mid_element]:
#                 # If target is in the right part of the sorted left half or not in the left half
#                 if target > nums[mid_element] or target < nums[left]:
#                     left = mid_element + 1 # Search in the right half
#                 else:
#                     right = mid_element - 1 # Search in the left half
#             # If the right half is sorted
#             else :
#                 # If target is in the left part of the sorted right half or not in the right half
#                 if target < nums[mid_element] or target > nums[right]:
#                     right = mid_element -1 # Search in the left half
#                 else :
#                     left = mid_element + 1 # Search in the right half
#         # If target is not found, return -1
#         return -1 
    
    
    
#     # Time -> O(logn)
    
#     # Space -> O(1) 
            

