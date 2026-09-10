# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        sm = 0
        count = 0

        def sum(root):
            nonlocal sm, count
            if not root:
                return
            sm += root.val
            count += 1
            sum(root.right)
            sum(root.left)

        def check(root):
            if not root:
                return 0

            nonlocal sm, count
            sm = 0
            count = 0

            sum(root)

            if sm // count == root.val:
                return 1 + check(root.left) + check(root.right)

            return check(root.left) + check(root.right)

        return check(root)
            
                

            