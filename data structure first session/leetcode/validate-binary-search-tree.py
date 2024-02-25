# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validet(root):
            nonlocal prev,result
            if not root:
                return 
            validet(root.left)
            if prev >= root.val:
                result = False
                #return
            # else:
            #     result = True
            #     return
            prev = root.val
            
            validet(root.right)
            return result
        result = True
        prev = float("-inf")
        return validet(root)
