# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            q = deque([root] if root else [])
            ans = []

            while q:
                level = []
                for i in range(len(q)):
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                ans.append(level)
            for i in range(len(ans)):
                if i %2!=0:
                    ans[i] = ans[i][::-1]
            return ans

