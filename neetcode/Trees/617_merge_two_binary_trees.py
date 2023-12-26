from typing import Optional

from neetcode import TreeNode, create_binary_tree_structure
from neetcode.Trees import print_binary_tree_structure


def merge_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 and not root2:
        return None
    elif root1 and not root2:
        return root1
    elif not root1 and root2:
        return root2

    left_merged = merge_trees(root1.left, root2.left)
    right_merged = merge_trees(root1.right, root2.right)

    return TreeNode(val=(root1.val + root2.val), left=left_merged, right=right_merged)


if __name__ == '__main__':
    inputs = [
        # ([1], [2]),
        ([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7]),
    ]
    for input_ in inputs:
        merged_tree = merge_trees(create_binary_tree_structure(input_[0]), create_binary_tree_structure(input_[1]))
        print_binary_tree_structure(merged_tree)
