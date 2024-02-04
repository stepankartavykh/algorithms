from typing import Optional

from neetcode import TreeNode, print_binary_tree_structure


def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    # TODO preorder - node.val + traversal(left) + traversal(right)
    # TODO inorder - traversal(left) + node.val + traversal(right)

    root = TreeNode(val=preorder[0])


    return root


if __name__ == '__main__':
    inputs = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
        ([-1], [-1]),
    ]
    for input_ in inputs:
        print(print_binary_tree_structure(build_tree(input_[0], input_[1])))
