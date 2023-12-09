from typing import Optional

from neetcode.Trees import TreeNode, create_binary_tree_structure


def tree2str(root: Optional[TreeNode]) -> str:
    if not root:
        return ''

    left = tree2str(root.left)
    right = tree2str(root.right)
    if len(right):
        if len(left):
            return ''.join([str(root.val), '(', left, ')', '(', right, ')'])
        else:
            return ''.join([str(root.val), '()', '(', right, ')'])
    else:
        if len(left):
            return ''.join([str(root.val), '(', left, ')'])
        else:
            return ''.join([str(root.val)])


def tree2str_stack_solution(root: Optional[TreeNode]) -> str:
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


if __name__ == "__main__":
    trees = [create_binary_tree_structure(elem) for elem in [
        [1, 2, 3, 4],
        [1, 2, 3, None, 4],
        [1, None, 4],
    ]]
    for elem in trees:
        print(tree2str(elem))
