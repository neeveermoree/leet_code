# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        elif s is not None and t is not None:
            if s.val == t.val:
                return self.isSubtree(s.left, t.left) and self.isSubtree(s.right, t.right)
            else:
                return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return False


"""
            3
        4       5
    1       2



            3
                5
"""