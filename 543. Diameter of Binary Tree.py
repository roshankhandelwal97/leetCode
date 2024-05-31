#https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        l_diameter = [0]

        def dfs(root):
            if root is None: 
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            d = left + right

            l_diameter[0] = max(d, l_diameter[0])

            return 1 + max(left, right)
        
        dfs(root)
        return l_diameter[0]


        
