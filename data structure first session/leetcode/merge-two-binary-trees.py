# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
            if root1 and root2:
                root3 = TreeNode(root1.val+root2.val)
                root3.left = self.mergeTrees(root1.left,root2.left) 
                root3.right = self.mergeTrees(root1.right,root2.right)
                return root3
            elif root1 :
                # root3.left = mergeTree(root1.left,root2)
                # root3.right = mergeTree(root1.right,root2)
                return root1
            elif root2:
                # root3.left = mergeTree(root1,root2.left)
                # root3.right = mergeTree(root1,root2.right)
                return root2
            
           
        
        # return mergeTree(root1,root2)
