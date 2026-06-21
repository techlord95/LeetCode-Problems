from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # using zip to keep the position and speed together
        
        cars = [(p,s) for p,s in zip(position,speed)]
        cars.sort(reverse=True) # sorts by position to process the cars closest to the target first in order to 
        # compare back of the cars with the fleets ahead , a car can only merge with cars ahead
        stack = []
        
        for p , s  in cars:
            stack.append((target - p) / s) # the time a car would take if unobstructed 
            
            # if the new time t <= time of the fleet ahead , it will catch (possibly at the target)
            # append followed by pop is way to ignore this t
            
            #we need at least 2 cars to compare, stack[-1] is the current car (behind) stack[-2] -> fleet ahead 
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop() # discarding the rear car's identity 
        return len(stack)
        
        
# postiion(p) , speed(s)        
   
# | Car (p,s) | t = (12-p)/s | stack after append | condition `stack[-1] <= stack[-2]` |               stack after possible pop |
# | --------- | -----------: | -----------------: | ---------------------------------: | -------------------------------------: |
# | (10,2)    |          1.0 |             [1.0] |                       — (only one) |                                 [1.0] |
# | (8,4)     |          1.0 |        \[1.0, 1.0] |                  1.0 <= 1.0 → True |                        [1.0] (merged) |
# | (5,1)     |          7.0 |        \[1.0, 7.0] |                 7.0 <= 1.0 → False |                            [1.0, 7.0] |
# | (3,3)     |          3.0 |   \[1.0, 7.0, 3.0] |                  3.0 <= 7.0 → True | [1.0, 7.0] (merged into second fleet) |
# | (0,1)     |         12.0 |  \[1.0, 7.0, 12.0] |                12.0 <= 7.0 → False |                      [1.0, 7.0, 12.0] |


# What zip Does Conceptually

# zip(position, speed) creates a struct-like binding:

# [(10,2), (8,4)]

# Now each tuple is:

# an atomic unit of computation

# This is equivalent to defining:

# class Car:
#     def __init__(self, p, s):
#         self.position = p
#         self.speed = s

# So zip is not just convenience—it’s:

# restoring entity integrity before transformation (sorting)


# TIME - O(nlogn)
# SPACE - O(n)

# Topics -> greedy , monotonic stack

