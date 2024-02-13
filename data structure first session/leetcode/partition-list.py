# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        right = ListNode()
        large = right
        left = ListNode()
        small = left
        while head:
            if head.val < x:
                small.next = head
                small = small.next
                
                #small = small.val
            else:
                large.next = head
                large = large.next
                #large = large.val
            head = head.next

        large.next = None
        small.next = right.next
        return left.next