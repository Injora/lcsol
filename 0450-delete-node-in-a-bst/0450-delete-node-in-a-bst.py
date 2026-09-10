# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root :
            return
        def search(root,key,parent):
            if root is None :
                return [None, None]
            if root.val == key :
                return [root,parent]
            if root.val>key :
                return search(root.left,key,root)
            if root.val<key :
                return search(root.right,key,root)
        found, parent = search(root,key,None)[0],search(root,key,None)[1]
        if found is None :
            return root
        if parent is None:
            if found :
                if found.left and found.right :
                    l = found.left
                    r = found.right
                    x = l
                    while x.right :
                        x=x.right
                    x.right = r
                    return l 
                if found.left :
                    return found.left
                else :
                    return found.right
        if found.right and found.left :
            l = found.left
            r = found.right
            x = l
            while x.right :
                        x=x.right
            x.right = r
            if parent.right == found :
                parent.right = l
                return root
            if parent.left == found :
                parent.left = l
                return root
        if found.left :
            l = found.left
            r = found.right
            if parent.right == found :
                parent.right = l
                return root
            else :
                parent.left = l
                return root
        else :
            l = found.left
            r = found.right
            if parent.right == found :
                parent.right = r
                return root
            else :
                parent.left = r
                return root



            
            