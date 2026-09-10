# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l = []

        def t(root):
            nonlocal l

            if not root:
                return

            t(root.left)
            l.append(root)
            t(root.right)

        t(root)

        l2 = []

        for i in range(len(l)):
            l2.append(l[i].val)

        l2.sort()

        an1 = -1
        an2 = -1

        for i in range(len(l)):
            if l[i].val != l2[i]:
                if an1 == -1:
                    an1 = i
                else:
                    an2 = i

        l[an1].val, l[an2].val = l[an2].val, l[an1].val


                
