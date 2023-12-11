from typing import Optional

from neetcode import TreeNode, create_binary_tree_structure


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == '__main__':
    trees = [create_binary_tree_structure(elem) for elem in [
        [1, 2, 3],
        [1, 2, 3, 2],
        [1],
        [2],
        [1, 2],
        [1, None, 2],
        [1, 2, 1],
        [1, 1, 2]
    ]]
    for tree_index in range(0, len(trees), 2):
        print(is_same_tree(trees[tree_index], trees[tree_index + 1]))
