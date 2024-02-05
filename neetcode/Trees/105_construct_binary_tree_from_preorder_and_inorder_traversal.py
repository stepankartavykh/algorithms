from typing import Optional

from neetcode import TreeNode, print_binary_tree_structure


def build_tree_neetcode_solution(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = build_tree_neetcode_solution(preorder[1: mid + 1], inorder[:mid])
    root.right = build_tree_neetcode_solution(preorder[mid + 1:], inorder[mid + 1:])
    return root


def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if not len(preorder):
        return None
    elif len(preorder) == 1:
        return TreeNode(val=preorder[0])

    root = TreeNode(val=preorder[0])
    ind = inorder.index(preorder[0])

    root.left = build_tree(preorder[1:ind + 1], inorder[0:ind])
    root.right = build_tree(preorder[ind + 1:], inorder[ind + 1:])

    return root


if __name__ == '__main__':
    inputs = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
        ([-1], [-1]),
        ([3, 9, ], [9, 3]),
    ]
    for input_ in inputs:
        print_binary_tree_structure(build_tree(input_[0], input_[1]))
        print('=' * 100)
