from typing import Optional

from neetcode import TreeNode, create_binary_tree_structure


def max_path_sum(root: Optional[TreeNode]) -> int:
    result = root.val

    def dfs(node):
        nonlocal result
        if not node:
            return 0

        left_max = max(dfs(node.left), 0)
        right_max = max(dfs(node.right), 0)

        result = max(result, node.val + left_max + right_max)
        return node.val + max(left_max, right_max)

    dfs(root)

    return result


if __name__ == '__main__':
    trees = [create_binary_tree_structure(elem) for elem in [
        [1, 2, 3],
        [-10, 9, 20, None, None, 15, 7],
        [10, -2, 3],
        [-2, -1],
        [2, -1],
        [1, -2, -3, 1, 3, -2, None, -1],
    ]]
    for tree in trees:
        print(max_path_sum(tree))
