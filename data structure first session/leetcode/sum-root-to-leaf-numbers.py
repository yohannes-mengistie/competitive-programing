# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
       
        def helper(root,result):
           
            if not root:
                return 0
            result = result*10 + root.val
            if not root.left and not root.right:
                return result
            return helper(root.left,result) + helper(root.right,result)
          
        
        return helper(root,0)
            