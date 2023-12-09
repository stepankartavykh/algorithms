from typing import Optional

from neetcode.Trees import TreeNode, create_binary_tree_structure


def preorder_traversal_iterative_solution(root: Optional[TreeNode]) -> list[int]:
    current = root
    stack = []
    result = []
    while current or stack:
        if current:
            result.append(current.val)
            stack.append(current.right)
            current = current.left
        else:
            current = stack.pop()
    return result


def preorder_traversal_recursive(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    left, right = preorder_traversal_recursive(root.left), preorder_traversal_recursive(root.right)
    return [root.val] + left + right


if __name__ == '__main__':
    trees = [create_binary_tree_structure(elem) for elem in [
        [1, None, 2, 3],
        [1, 2, 5, 3, 4, 6, 7],
        [],
        [1],
        [1, None, 5, None, None, None, 7]
    ]]
    for elem in trees:
        print(preorder_traversal_iterative_solution(elem))
