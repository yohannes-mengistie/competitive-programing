# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def maxdiff(root,min_val,max_val):
    
            if not root:
                return max_val - min_val
            
          
            min_val = min(min_val,root.val)
            max_val = max(max_val,root.val)
            left =  maxdiff(root.left , min_val,max_val)
            right = maxdiff(root.right,min_val,max_val)
            return max(left,right)
        return maxdiff(root,root.val,root.val)
            
        