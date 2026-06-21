# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

# Reverse & Merge 
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ptr1 , ptr2 = head , head 
        
        while ptr2 and ptr2.next :
            ptr1 = ptr1.next 
            ptr2 = ptr2.next.next 
            
            # pointer for second half of the list 
            second = ptr1.next 
            
            # setting to null 
            prev = ptr1.next = None 
            
            # reversing the second portion of the list , while second is non empty 
            while second: 
                temp = second.next 
                second.next = prev 
                prev = second
                second = temp 
            
            # merging the two halves    
            first , second  = head , prev 
            
            while second :
                temp1 , temp2 = first.next , second.next 
                first.next = second
                second.next = temp1 
                first , second = temp1 , temp2 
                
# Time -> O(n) 
# Space -> O(1)

# approach -> 
# mmerging linked list in 2 halves , irrespective of even or odd 
# idea is to have pointer at the first node then break the node to have the element of the second half of the list 
# while breaking the length of the node we have to store it using temp variables 
            
     