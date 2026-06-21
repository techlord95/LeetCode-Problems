# class ListNode():
#     def LinkedListNode(self ,val=0, next = None):
#         self.val = val 
#         self.next = next 

from typing import Optional
class Solution():
    def hasCycle(self ,head: Optional[ListNode]) -> bool:
        
        # 1 moves at 1 step at a time , 2 moves at 2 steps at a time
        pointer1 , pointer2  = head , head 
        
        while pointer2 and pointer2.next:
            pointer1 = pointer1.next # 1 step 
            pointer2 = pointer2.next.next  # 2 steps 
            
            if pointer1 == pointer2:
                return True 
        return False
    
# Time  O(n) 
# Space O(1)