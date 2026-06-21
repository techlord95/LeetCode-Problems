class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        
        #checking the empty array
        if not nums:
            return 0 
        
        #using set to get a unique elements array since the set is unordered the results are not always sorted 
        sorted_nums_set = set(nums)
        longest = 0 # start longest sequence count 
        
        #iterating through each unique element in set 
        for num in sorted_nums_set:
            if num -1 not in sorted_nums_set: # checks if the previous number in the sequence exists , if it does then it is in a middle of the sequence (left , num ,right)
                current = num # keeps track of current number 
                
                streak = 1 # number will contain itself to start a sequence 
                
                while current + 1 in sorted_nums_set: # cur+1 is the next consecutive element in the set 
                    current +=1 
                    streak +=1 # if it does then extend the streak 
                    
                longest = max(longest, streak) # to update the current longest streak and the streak that was just found 
        return longest
    
    
Time and Space -> O(n)

inst= Solution()
arr = [2,5,4,3,8,9,10,11,12,13]
v=inst.longestConsecutive(arr)
print(v)
        
        
        
        