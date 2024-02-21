# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prv,cur = dummy,dummy.next
        while cur:
            if cur.val == val :
                cur = cur.next
                prv.next = cur
            else:
                prv,cur = cur,cur.next
        return dummy.next

        