# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        def merge(dummy,node1,node2):
            if node1 == None:
                return node2
            if node2 == None:
                return node1
            if node1.val < node2.val:
                dummy = node1
                dummy.next = merge(dummy,node1.next,node2)
            else:
                dummy = node2
                dummy.next = merge(dummy,node1,node2.next)
            return dummy
        return merge(dummy,list1,list2)