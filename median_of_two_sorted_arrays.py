from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        # making sure the binary search happens on the smallest array minimum(O(logn))
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        
        # i is the cut index in A (mid of l and r)
        while True:
            i = (l + r) // 2
            # total elements on the left of both arrays equals half 
            j = half - i - 2  # this was suppposed to be j = half - (i + 1) - 1 , i+1 as the index starts from 1 

            Aleft = A[i] if i >= 0 else float("-infinity") # if less than 0 then its out of bound
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity") # float is used as the infinity is a str type 
            Bleft = B[j] if j >= 0 else float("-infinity") # same as Bleft 
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity") 
            
            # this means partition is correct 
            if Aleft <= Bright and Bleft <= Aright: # will give error here if float is not used str != int 
                #odd 
                if  total % 2:
                    return min(Aright, Bright)
                # even 
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # partition is too far right
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
                
# A = [1, 3, 7, 10]
# i = 1 

# Partition looks like 
# 1 3 | 7 10
#     ^
#     i

# Aleft  = A[i]     = 3
# Aright = A[i + 1] = 7

# left partition size = i + 1 , as indices start from 0 


# j represents the same thing for B 

# B = [2, 4, 5, 8, 9]
# j = 2 

# 2 4 5 | 8 9
#       ^
#       j

# Bleft  = B[j]     = 5
# Bright = B[j + 1] = 8


# why we need j = half - i - 2 , bc the total number of elements on the left side must 
# always be equal half 

# (A left size) + (B left size) = half