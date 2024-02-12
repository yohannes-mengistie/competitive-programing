# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        ans = []
        while cur:
            ans.append(cur.val)
            cur = cur.next

      
        if ans[::-1] == ans:
            return True
        else:
            return False
        