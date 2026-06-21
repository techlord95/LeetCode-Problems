# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':