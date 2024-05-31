#https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        temp = [0]
        def height(root):
            if root is None: 
                return 0
            l = height(root.left)
            r = height(root.right)

            if(abs(l-r)) > 1: 
                temp[0] = 1

            return 1 + max(l, r)
        height(root)
        if temp[0] == 1: 
            return False
        else: return True

        
