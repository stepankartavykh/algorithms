from typing import Optional, List

from neetcode import TreeNode, create_binary_tree_structure


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    # TODO There is better solution!
    result = []

    stack = [[root]]
    while stack and stack[0]:
        current_level = stack.pop()
        right_node = current_level[-1]
        if right_node:
            result.append(right_node.val)
        else:
            break
        cur_level = []
        for r in current_level:
            if r.left:
                cur_level.append(r.left)
            if r.right:
                cur_level.append(r.right)
        stack.append(cur_level)
    return result


if __name__ == '__main__':
    print(right_side_view(create_binary_tree_structure([1, 2, 3, None, 5, None, 4])))
