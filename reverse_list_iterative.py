from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        prev = None
        while(head.next is not None):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            
        head.next = prev
        return head