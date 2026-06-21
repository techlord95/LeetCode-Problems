# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # initial node is the dummy node to avoide edge case of being an empty node
        initial_node = node = ListNode() #node is the pointer used to build the new list 
        
        
        while list1 and list2 : 
            if list1.val < list2.val:
                # attaching list1 node to result 
                node.next = list1 
                # movin list1 forward
                list1 = list1.next  
            else:
                node.next = list2 
                list2 = list2.next 
            # moving node forward , to append 
            node = node.next 
           
        # till here one list is fully exhausted . other still has sorted nodes left which can be directly attached  
        node.next = list1 or list2
         
        return initial_node.next
            
        
# time -> O(n+m)
# space -> O(1) 