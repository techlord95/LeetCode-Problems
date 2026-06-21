class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        
        for i in range(n):
            #ignoring the negative nums , after and it checks if the nums are already in the correct slot 
            # eg in first test case 3 should be at index 3 not 0 
            
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                
                # Swap nums[i] to its correct index
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # Step 2: Find the first index where nums[i] != i+1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: If all are correct, smallest missing = n+1
        return n + 1

# Time = O(n)

# Space = O(1) auxiliary space.
    
