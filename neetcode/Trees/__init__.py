from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode(val={self.val})'


def create_binary_tree_structure(values: List[int]) -> Optional[TreeNode]:
    if not values:
        return None

    it = iter(values)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root


def print_binary_tree_structure(root: Optional[TreeNode], level=0) -> None:
    if root is None:
        return

    print_binary_tree_structure(root.right, level + 1)
    print('  ' * level + str(root.val))
    print_binary_tree_structure(root.left, level + 1)
