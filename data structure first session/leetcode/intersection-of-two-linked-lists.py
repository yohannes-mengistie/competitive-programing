# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length1 = 0
        cur = headA
        while cur and cur.next:
           
            length1 +=1
            cur = cur.next

        length2 = 0
        cur =  headB
        while cur and cur.next:
            
            length2 +=1
            cur = cur.next

        dif = abs(length1-length2)

        if length1 > length2:
            pointerA = headA
            while dif > 0 and pointerA:
                pointerA = pointerA.next
                dif -=1

            pointerB = headB
            while pointerB and pointerA and pointerA != pointerB:
                pointerA = pointerA.next
                pointerB = pointerB.next

            return pointerB
        else:
            pointerB = headB
            while dif > 0 and pointerB:
                pointerB = pointerB.next
                dif -=1

            pointerA = headA
            while pointerB and pointerA and pointerA != pointerB:
                pointerA = pointerA.next
                pointerB = pointerB.next

            return pointerA


