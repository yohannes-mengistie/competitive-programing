# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        leftPrv,cur = dummy,dummy.next
        for i in range(left-1):
            leftPrv,cur = cur,cur.next
        prv = None
        for j in range(right-left+1):
            tmp = cur.next
            cur.next = prv
            prv,cur = cur,tmp

        
        leftPrv.next.next = cur
        leftPrv.next = prv
        return dummy.next

        
    

            
