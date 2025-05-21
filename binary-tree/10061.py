class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minimum(root):
    while root.left:
        root = root.left
    return root
