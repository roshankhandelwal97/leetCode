#https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return None
            
        res= []

        if not root: 
            return []

        q = deque([root])

        while q: 
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            res.append(temp)
        return res

        
