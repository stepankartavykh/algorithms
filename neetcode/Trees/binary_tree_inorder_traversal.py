from collections import deque
from typing import Optional, List

from neetcode.Trees import TreeNode, create_binary_tree_structure


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    left_part = inorder_traversal(root.left)
    right_part = inorder_traversal(root.right)
    return left_part + [root.val] + right_part


def iterative_inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res = []
    roots = deque([root])
    while roots:
        for r in range(len(roots)):
            node = roots.popleft()
            if node.left:
                roots.append(node.left)
            if node.right:
                roots.append(node.right)


if __name__ == '__main__':
    binary_structure = create_binary_tree_structure([1, None, 2, 3])
    print(inorder_traversal(binary_structure))
