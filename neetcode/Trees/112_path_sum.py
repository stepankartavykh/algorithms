from typing import Optional

from neetcode import TreeNode, create_binary_tree_structure


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:

    def search_path(node, current_sum):
        if not node:
            return False
        current_sum_internal = current_sum + node.val
        if not node.left and not node.right:
            if current_sum_internal == target_sum:
                return True
        left = search_path(node.left, current_sum_internal)
        right = search_path(node.right, current_sum_internal)

        return left or right

    return search_path(root, 0)


if __name__ == '__main__':
    trees = [create_binary_tree_structure(elem) for elem in [
        [],
        [1, 2, 3],
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
    ]]
    print(has_path_sum(trees[0], 0))
    print(has_path_sum(trees[1], 3))
    print(has_path_sum(trees[2], 22))
