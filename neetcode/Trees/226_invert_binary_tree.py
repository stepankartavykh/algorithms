from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:

    left, right = root.left, root.right
    left, right = root.left, root.right
    if left is None and right is None:
        return root
    left_left, left_right = left.left, left.right
    right_left, right_right = right.left, right.right
