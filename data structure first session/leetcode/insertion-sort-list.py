# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prv,cur = head,head.next
        while cur:
            if cur.val>=prv.val:
                prv,cur=cur,cur.next
                continue
            temp = dummy
            while cur.val > temp.next.val:
                temp = temp.next
            
            prv.next = cur.next
            cur.next = temp.next
            temp.next = cur
            cur = prv.next
        return dummy.next