from typing import Optional

from neetcode import TreeNode, create_binary_tree_structure
# TODO iterative solution


def k_th_smallest(root: Optional[TreeNode], k: int) -> int:
    # TODO may be is there a batter way? It's not readable.
    counter = 0
    result = 10 ** 4

    def traversal(node):
        nonlocal counter, result
        if not node:
            return
        traversal(node.left)
        counter += 1
        if counter == k:
            result = node.val
            return
        traversal(node.right)

    traversal(root)

    return result


if __name__ == '__main__':
    params = [(create_binary_tree_structure(elem[0]), elem[1]) for elem in [
        ([3, 1, 4, None, 2], 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3)
    ]]
    for elem in params:
        print(k_th_smallest(elem[0], elem[1]))
