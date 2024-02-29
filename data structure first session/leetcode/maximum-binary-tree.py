# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
       
        def recursion(nums):
            if len(nums) == 0:
                return None
            max_val = max(nums)
            ind = nums.index(max_val)
            r = TreeNode(max_val)
           
               
            r.left = recursion(nums[0:ind])
            r.right = recursion(nums[ind+1:])
            return r
        return recursion(nums)

