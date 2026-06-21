
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

# from typing import Optional
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
#         if head is None:
#             return None 
        
#         # l1 is original node 
#         l1 = head 
        
#         # creating copies and inserting them after original nodes 
#         while l1:
#             l2 = Node(l1.val) # l2 is the copy node 
#             l2.next = l1.random 
#             l1.random = l2 
#             l1 = l1.next 
            
#         # storing new head 
#         newHead = head.random
        
#         # assigning random pointers of copied nodes 
#         l1 = head 
#         while l1:
#             l2 = l1.random 
#             l2.random = l2.next.random if l2.next else None 
#             l1 = l1.next 
         
#         # separating original and copied lists   
#         l1 = head 
#         while l1 is not None:
#             l2 = l1.random 
#             l1.random = l2.next 
#             l2.next = l1.next.random if l1.next else None
#             l1 = l1.next 
            
#         return newHead
    
## Time -> O(n)
## Space -> O(1) extra space 



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':   
        
        # creating a hashmap 
        old_to_copy = {None:None}    # mapping old node  to copy 
        
        # current pointer pointing to the head 
        current = head 
        
        # this is the first pass of the loop , here we are cloning the linked list nodes and adding it to the hashmap
        while current:
            copy = Node(current.val)
            old_to_copy[current] = copy # mapping the old node to copy node
            current = current.next # updating the curr pointer until it becomes null
            
        current = head 
        while current:
            copy = old_to_copy[current]
            copy.next = old_to_copy[current.next]  # if curr.next is null (we add none in old to copy) in line 63 
            copy.random = old_to_copy[current.random]
            current = current.next 
            
            
        return old_to_copy[head]
            
        
            
            

        
        