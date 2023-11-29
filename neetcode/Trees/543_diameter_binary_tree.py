from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    def max_depth(r: Optional[TreeNode]) -> int:
        if not r:
            return 0
        left_depth = max_depth(r.left)
        right_depth = max_depth(r.right)
        return 1 + max(left_depth, right_depth)

    if not root:
        return 1

    return max_depth(root.left) + max_depth(root.right)
