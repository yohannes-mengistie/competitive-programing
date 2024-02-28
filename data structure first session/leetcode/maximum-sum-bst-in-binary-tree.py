# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(node):
            nonlocal ans
            if not node.left and not node.right:
                ans=max(ans,node.val,node.val)
                return node.val,node.val,node.val
            leftsum,leftmin,leftmax = 0,node.val,-math.inf
            if node.left:
                leftsum,leftmin,leftmax = helper(node.left)
            rightsum,rightmin,rightmax = 0,math.inf,node.val
            if node.right:
                rightsum,rightmin,rightmax = helper(node.right)

            if leftmax <node.val<rightmin:
                cur = leftsum+rightsum+node.val
                ans = max(ans,cur)
                return cur,leftmin,rightmax
            else:
                return 0,-math.inf,math.inf
        helper(root)
        return ans