class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def next_node(root, x):
    node = find(root, x)
    if node.right:
        return minimum(node.right)
    successor = None
    while root:
        if x < root.val:
            successor = root
            root = root.left
        elif x > root.val:
            root = root.right
        else:
            break
    return successor
