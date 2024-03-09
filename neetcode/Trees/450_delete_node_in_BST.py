from collections import deque

from neetcode import TreeNode, create_binary_tree_structure, print_binary_tree_structure


def deleteNode(root: TreeNode | None, key: int) -> TreeNode | None:
    if not root:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        min_node_in_right = root.right
        while min_node_in_right.left:
            min_node_in_right = min_node_in_right.left

        # TODO analyze this place again!
        root.val = min_node_in_right.val
        root.right = deleteNode(root.right, root.val)

    return root


def delete_node_second(root: TreeNode | None, key: int) -> TreeNode | None:
    if not root:
        return root

    if key < root.val:
        root.left = delete_node_second(root.left, key)
        return root

    if key > root.val:
        root.right = delete_node_second(root.right, key)
        return root

    if not root.right:
        return root.left

    current = root.right
    while current.left:
        current = current.left

    current.left = root.left
    return root.right


def deleteNode_iterative(root: TreeNode | None, key: int) -> TreeNode | None:
    stack = deque([root])

    while stack:
        current = stack.pop()


if __name__ == '__main__':
    inputs = [
        ([2, 1, 3], 2),
        ([5, 3, None, 2, 4], 3),
        ([5, 3, 6, 2, 4, None, 7], 3),
        ([5, 3, 6, 2, 4, None, 7], 0),
    ]
    for input_ in inputs:
        tree = create_binary_tree_structure(input_[0])
        key = input_[1]
        print_binary_tree_structure(deleteNode(tree, key))
