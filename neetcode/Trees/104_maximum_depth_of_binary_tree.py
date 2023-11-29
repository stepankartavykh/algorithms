from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)


def max_depth_bfs(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    level = 1
    roots = deque([root])
    while roots:
        for index in range(len(roots)):
            node = roots.popleft()
            if node.left:
                roots.append(node.left)
            if node.right:
                roots.append(node.right)
        level += 1
    return level


def max_depth_dfs(root: Optional[TreeNode]) -> int:
    stack = [(root, 1)]
    res = 0
    while stack:
        node, d = stack.pop()
        if node:
            res = max(res, d)
            stack.append((node.left, d + 1))
            stack.append((node.right, d + 1))
    return res
