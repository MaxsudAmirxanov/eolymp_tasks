class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_elements(root):
    if not root:
        return 0
    return root.val + sum_elements(root.left) + sum_elements(root.right)
