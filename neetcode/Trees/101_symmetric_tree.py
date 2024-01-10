from collections import deque
from typing import Optional

from neetcode import TreeNode, create_binary_tree_structure


def is_symmetric_my_solution(root: Optional[TreeNode]) -> bool:
    deq = deque([root])

    while deq:
        t_deq = deque()
        while deq:
            node = deq.popleft()
            if node:
                t_deq.append(node.left)
                t_deq.append(node.right)
            else:
                t_deq.append(None)
                t_deq.append(None)
        for index in range(len(t_deq) // 2):
            left_side_node = t_deq[index]
            right_side_node = t_deq[len(t_deq) - index - 1]
            if (not left_side_node and right_side_node) or (left_side_node and not right_side_node):
                return False
            if left_side_node and right_side_node and (left_side_node.val != right_side_node.val):
                return False
        if not any(t_deq):
            deq = deque()
        else:
            deq = t_deq
    return True


def is_symmetric(root: Optional[TreeNode]) -> bool:
    def func(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return func(p.left, q.right) and func(p.right, q.left)

    return func(root.left, root.right)


if __name__ == '__main__':
    trees = [create_binary_tree_structure(elem) for elem in [
        [1, 2, 2],
        [1, 2, 2, 3, 4, 4, 3],
        [1, 2, 2, None, 3, None, 3],
        [1, 2, 2, None, 3, 3]
    ]]
    for tree_index in range(len(trees)):
        print(is_symmetric(trees[tree_index]))
