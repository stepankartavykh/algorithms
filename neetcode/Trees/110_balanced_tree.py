from typing import Optional

from neetcode.Trees import create_binary_tree_structure, TreeNode


def is_balanced(root: Optional[TreeNode]) -> bool:
    def func(root_: Optional[TreeNode]):
        if not root_:
            return True, 0

        left, right = func(root_.left), func(root_.right)

        if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
            return True, 1 + max(left[1], right[1])
        return False, 0

    return func(root)[0]


if __name__ == '__main__':
    sets = [
        [3, 9, 20, None, None, 15, 7],
        [1, 2, 2, 3, 3, None, None, 4, 4]
    ]
    trees = [create_binary_tree_structure(value) for value in sets]

    print(is_balanced(trees[0]) is True)
    print(is_balanced(trees[1]) is False)
