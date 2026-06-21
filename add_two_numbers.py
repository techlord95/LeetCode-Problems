# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

# iterative approach
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        current = dummy_node 
        
        carry = 0 
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l1 else 0
            
            # New Digit 
            value = val1 + val2 + carry
            
            carry = value // 10 # floor division returns quotient 
            
            value = value % 10 # modulus remainder 
            
            current.next = ListNode(value)
            
            # Updating Pointers 
            
            current = current.next 
            l1 = l1.next if l1 else 0 
            l2 = l2.next if l1 else 0
        return dummy_node.next
    
# This works below 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        current = dummy 

        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
            value = val1 + val2 + carry 

            carry = value // 10 
            value = value % 10 
            current.next = ListNode(value)
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 

        return dummy.next
        
        