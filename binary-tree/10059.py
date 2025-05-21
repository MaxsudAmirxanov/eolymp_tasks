class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    return sum_leaves(root.left) + sum_leaves(root.right)
