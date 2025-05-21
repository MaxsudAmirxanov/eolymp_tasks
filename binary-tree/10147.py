class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def previous_node(root, x):
    node = find(root, x)
    if node.left:
        return maximum(node.left)
    predecessor = None
    while root:
        if x < root.val:
            root = root.left
        elif x > root.val:
            predecessor = root
            root = root.right
        else:
            break
    return predecessor
