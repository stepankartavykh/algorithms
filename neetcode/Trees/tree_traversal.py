from typing import Optional, List

from neetcode import TreeNode


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    left, right = inorder_traversal(root.left), inorder_traversal(root.right)
    return left + [root.val] + right


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    left, right = inorder_traversal(root.left), inorder_traversal(root.right)
    return [root.val] + left + right


def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    left, right = inorder_traversal(root.left), inorder_traversal(root.right)
    return left + right + [root.val]
