from neetcode import TreeNode, create_binary_tree_structure


def insertIntoBST_new(root: TreeNode | None, val: int) -> TreeNode | None:
    if not root:
        return TreeNode(val=val)

    def traverse_tree(node: TreeNode | None):
        if val < node.val and not node.left:
            node.left = TreeNode(val=val)
            return
        if val < node.val and node.left:
            traverse_tree(node.left)
            return
        if val > node.val and not node.right:
            node.right = TreeNode(val=val)
            return
        if val > node.val and node.right:
            traverse_tree(node.right)
            return
        if not node.left and not node.right:
            if val < node.val:
                node.left = TreeNode(val=val)
            else:
                node.right = TreeNode(val=val)
            return

    traverse_tree(root)

    return root


if __name__ == '__main__':
    trees = [
        ([4, 2, 7, 1, 3], 5),
        ([40, 20, 60, 10, 30, 50, 70], 25),
        ([4, 2, 7, 1, 3, None, None, None, None, None, None], 5),
        ([5, None, 14, 10, 77, None, None, None, 95, None, None], 4),
    ]
    for tree in trees:
        print(insertIntoBST_new(root=create_binary_tree_structure(tree[0]),
                                val=tree[1]))
