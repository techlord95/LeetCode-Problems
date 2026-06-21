# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        left = dummy
        
        right = head 
        
        while n>=1:
            right = right.next 
            n -=1 
        while right:
            left = left.next 
            right = right.next 
            
        # linked list 
        # l1 -> l2 -> l3 
        # breaking by moving to the next pointer     
            
        left.next = left.next.next  
        
        return dummy.next 
        
        
            
        