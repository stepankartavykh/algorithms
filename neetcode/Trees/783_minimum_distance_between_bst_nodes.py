from typing import Optional, List

from neetcode import TreeNode, create_binary_tree_structure


def min_diff_in_bst(root: Optional[TreeNode]) -> int:
    # TODO resolve this problem!
    min_diff = float('inf')
    previous = None

    def func(node):
        if not node:
            return
        nonlocal min_diff, previous
        func(node.left)
        if previous:
            min_diff = min(min_diff, node.val - previous.val)
        previous = node
        func(node.right)

    func(root)

    return min_diff


if __name__ == '__main__':
    inputs = [
        [4, 2, 6],
        [4, 2, 6, 1, 3],
        [1, 0, 48, None, None, 12, 49]
    ]
    for input_ in inputs:
        print(min_diff_in_bst(create_binary_tree_structure(input_)))
        print()
