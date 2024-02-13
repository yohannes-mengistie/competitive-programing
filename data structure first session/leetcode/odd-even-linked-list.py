# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next:
                return head
            left = head
            right = head.next
            rightHead = right

            while left.next and right.next:
                left.next = right.next
                left = right.next
                right.next = left.next
                right = left.next

            left.next = rightHead
            return head
        

         