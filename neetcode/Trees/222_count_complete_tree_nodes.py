from neetcode import TreeNode, create_binary_tree_structure


def count_nodes(root: TreeNode | None) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    elif root.right is None:
        return 2
    left_level = level(root.left)
    right_level = level(root.right)
    if left_level == right_level:
        return 2 ** left_level + count_nodes(root.right)
    else:
        return count_nodes(root.left) + 2 ** right_level


def level(root):
    i = 0
    while root:
        i += 1
        root = root.left
    return i


if __name__ == '__main__':
    print(count_nodes(create_binary_tree_structure([1, 2, 3, 4, 5, 6])))
