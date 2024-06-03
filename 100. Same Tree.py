#https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = [0]
        def dfs(p,q):

            if not p and not q: 
                return 
            if not p and q: 
                flag[0] = 1
                return
            if p and not q: 
                flag[0] = 1
                return
            if p.val != q.val:
                print("Inside if condition")
                flag[0] = 1
                return
        
            dfs(p.left, q.left)
            dfs(p.right, q.right)
        
        dfs(p,q)
        if flag[0] == 0: 
            return True
        else: 
            return False
            

            
            
            
