import math    
from collections import List         
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # eating speed cannot start from 0 
        l, r = 1, max(piles)
        res = r
        
        # binary search initiate
        while l <= r:
            k = (l + r) // 2
            #initiating hour from 0 
            totalTime = 0
            
            # float is not required 
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
    
# Time = O(n log m)
# Space = O(1)