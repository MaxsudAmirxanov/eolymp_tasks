class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maximum(root):
    while root.right:
        root = root.right
    return root
