from typing import Optional

from neetcode import TreeNode, create_binary_tree_structure


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    if not sub_root:
        return True
    if not root:
        return False
    if is_same_tree(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


if __name__ == '__main__':
    trees = [create_binary_tree_structure(elem) for elem in [
        [3, 4, 5, 1, 2],
        [4, 1, 2],
        [1, 2, 3, 4],
        [1, 2, 3]
    ]]
    for tree_index in range(0, len(trees), 2):
        print(is_subtree(trees[tree_index], trees[tree_index + 1]))
