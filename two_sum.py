class Solution:
    def twoSum(self, nums:list[int] , target:int) ->list[int]:
        for i in range(len(nums)):
            # i is already pointing to one number j checks numbers after it 
            for j in range(i + 1 , len(nums)): 
                if target == nums[i] + nums[j]:
                    return [i,j]

        
        
        
        

# # Time = O(n^2)
# # Space = O(1)

