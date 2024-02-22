# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inOrder(root):
            if not root:
                return 

            #return inOrder(root.left) + [root.val] + inOrder(root.right)
            if root.left:
               
                inOrder(root.left)
                # ans.append(root.left.val)
            if root:
                ans.append(root.val)
            if root.right:
                
                inOrder(root.right)
                # ans.append(root.right.val)

        ans = []
        inOrder(root)
        
        return ans
            