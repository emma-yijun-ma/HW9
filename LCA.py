def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
    return root if left and right else left or right
class TreeNode(object):

     def __init__(self, val=0, left=None, right=None):

         self.val = val

         self.left = left

         self.right = right
