import math
from typing import Optional
from neetcode import TreeNode, create_binary_tree_structure


def is_valid_binary_search_tree(root: Optional[TreeNode]) -> bool:
    def is_valid(node, left_boundary, right_boundary):
        if not node:
            return True
        if not left_boundary < node.val < right_boundary:
            return False
        return is_valid(node.left, left_boundary, node.val) and is_valid(node.right, node.val, right_boundary)

    return is_valid(root.left, -math.inf, root.val) and is_valid(root.right, root.val, math.inf)


if __name__ == '__main__':
    inputs = [
        [2, 1, 3],
        [5, 1, 4, None, None, 3, 6],
        [5, 1, 10, None, None, 6, 11],
        [5, 4, 6, None, None, 3, 7],
        [32, 26, 47, 19, None, None, 56, None, 27],
    ]

    for input_ in inputs:
        print(is_valid_binary_search_tree(create_binary_tree_structure(input_)))
