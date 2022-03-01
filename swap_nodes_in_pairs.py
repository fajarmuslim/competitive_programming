# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def helper(self, head: Optional[ListNode]):
        if (head is None) or (head.next is None):
            return head
        else:
            temp = head.val
            head.val = head.next.val
            head.next.val = temp
            self.helper(head.next.next)
            return head         
        
        
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ref_head = head
        return self.helper(head)