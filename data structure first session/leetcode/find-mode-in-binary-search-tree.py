# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}
        def recurce(root):
            if not root:
                return None
            recurce(root.left)
            recurce(root.right)
            if root.val in dic:
                dic[root.val] +=1
            else:
                dic[root.val] = 1
            
            
            
        recurce(root) 
        ans = []
        maxx_val = max(dic.values())
        ans =[i for i in dic if dic[i] == maxx_val]
        return ans

            
