from typing import List, Optional

from neetcode import TreeNode, print_binary_tree_structure


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    if not len(nums):
        return None
    center_position = len(nums) // 2
    root = TreeNode(val=nums[center_position])

    left, right = center_position - 1, center_position + 1
    root.left = sorted_array_to_bst(nums[0:left + 1])
    root.right = sorted_array_to_bst(nums[right:])

    return root


if __name__ == '__main__':
    inputs = [
        [-10, -3, 0, 5, 9],
        [1, 3]
    ]
    for input_ in inputs:
        print('=' * 100)
        print_binary_tree_structure(sorted_array_to_bst(input_))
