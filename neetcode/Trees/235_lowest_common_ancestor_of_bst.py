from neetcode import TreeNode, create_binary_tree_structure


def lowest_common_ancestor(root: TreeNode, p: int, q: int) -> int:
    if p < root.val < q or q < root.val < p or root.val == p or root.val == q:
        return root.val
    if p < root.val and q < root.val:
        return lowest_common_ancestor(root.left, p, q)
    if p > root.val and q > root.val:
        return lowest_common_ancestor(root.right, p, q)


def lowest_common_ancestor_second(root: TreeNode, p: int, q: int) -> int:
    while True:
        if root.val < p and root.val < q:
            root = root.right
        elif root.val > p and root.val > q:
            root = root.left
        else:
            return root.val


if __name__ == '__main__':
    inputs = [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4),
        ([2, 1], 2, 1)
    ]
    for input_ in inputs:
        print(lowest_common_ancestor_second(create_binary_tree_structure(input_[0]), input_[1], input_[2]))
