import dis
from typing import Optional


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def create_tree():
    left_node = TreeNode(val=2)
    right_node = TreeNode(val=4)
    head_tree = TreeNode(val=5, left=left_node, right=right_node)


if __name__ == '__main__':
    print(dis.dis(create_tree))
