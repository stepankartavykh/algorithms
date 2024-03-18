from neetcode import TreeNode, create_binary_tree_structure


def minDepth(root: TreeNode | None) -> int:
    # TODO Iterative solution also can be implemented. May be it will be more readable.
    if not root:
        return 0
    min_depth = float('inf')

    def dfs(node, depth):
        if not node:
            return

        nonlocal min_depth
        if node.left:
            dfs(node.left, depth + 1)
        if node.right:
            dfs(node.right, depth + 1)

        if not node.left and not node.right:
            min_depth = min(min_depth, depth)

    dfs(root, 1)

    return min_depth


if __name__ == '__main__':
    print(minDepth(create_binary_tree_structure([])))
    print(minDepth(create_binary_tree_structure([3, 9, 20, None, None, 15, 7])))
    print(minDepth(create_binary_tree_structure([2, None, 3, None, 4, None, 5, None, 6])))
