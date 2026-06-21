class Solution :
    def containsDuplicate(self,nums) -> bool:
        return (len(list(set(nums))) < len(nums))

# create an instance of a class
s = Solution()
nums = [1,2,3,2]
print(s.containsDuplicate(nums))




        