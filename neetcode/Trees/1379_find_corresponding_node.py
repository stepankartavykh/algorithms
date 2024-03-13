from neetcode import TreeNode


def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    if not original:
        return None

    if original is target:
        return cloned

    left = getTargetCopy(original.left, cloned.left, target)
    if left:
        return left
    right = getTargetCopy(original.right, cloned.right, target)
    if right:
        return right

    return None
