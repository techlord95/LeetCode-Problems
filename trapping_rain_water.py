class Solution:
    def trap(self, height: list[int]) -> int:
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0 # left_max to store the tallest bar seen till now from the left , same for right bar in right_max 
        water = 0 # this holds the water 
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left] #updating the left_max as no water is trapped at this point, this will happen when a taller bar is found on the left 
                else:
                    water += left_max - height[left] #if current bar is shorter than left_max water can be trapped here 
                left += 1 # moving the left pointer one step right 
                
            else: # if the right bar is shorter or == left bar 
                if height[right] >= right_max: # if the current right bar is taller or = (>=) right_max then 
                    right_max = height[right] # cont.-> we update the right max 
                else:
                    water += right_max - height[right]
                right -= 1 #moving the right pointer one step left
        
        return water
    
    
# Time = O(n)
# Space = O(1)



 