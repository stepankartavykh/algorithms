from neetcode import TreeNode, create_binary_tree_structure


def binaryTreePaths(root: TreeNode | None) -> list[str]:
    paths = []

    def dfs(node, path):
        if not node.left and not node.right:
            paths.append(path + str(node.val))
            return

        if node.left:
            dfs(node.left, path + str(node.val) + "->")
        if node.right:
            dfs(node.right, path + str(node.val) + "->")

    dfs(root, '')

    return paths


if __name__ == '__main__':
    print(binaryTreePaths(create_binary_tree_structure([1, 2, 3, None, 5])))
