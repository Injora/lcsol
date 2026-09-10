# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0

        def make(preorder, ub):
            nonlocal i

            if i == len(preorder) or preorder[i] > ub:
                return

            root = TreeNode(preorder[i])
            i += 1

            root.left = make(preorder, root.val)
            root.right = make(preorder, ub)

            return root

        return make(preorder, 100000000000)