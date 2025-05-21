class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find(root, x):
    if not root:
        return None
    if root.val == x:
        return root
    elif x < root.val:
        return find(root.left, x)
    else:
        return find(root.right, x)
