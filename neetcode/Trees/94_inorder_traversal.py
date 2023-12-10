from typing import Optional, List

from neetcode import TreeNode, create_binary_tree_structure


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    left, right = inorder_traversal(root.left), inorder_traversal(root.right)
    return left + [root.val] + right


def inorder_traversal_iterative_solution(root: Optional[TreeNode]) -> List[int]:
    #  TODO must be done!
    pass


if __name__ == '__main__':
    trees = [create_binary_tree_structure(elem) for elem in [
        [1, None, 2, 3],
        [1, 2, 3, 4, 5, None, 6],
    ]]
    for elem in trees:
        print(inorder_traversal(elem))
