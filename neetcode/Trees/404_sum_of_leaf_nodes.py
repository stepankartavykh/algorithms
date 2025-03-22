from neetcode.Trees import TreeNode, create_binary_tree_structure



def sumOfLeftLeaves(root: TreeNode | None) -> int:

    start_node = root

    def traverse(node, is_left_branch):
        if not node:
            return 0
        if not node.left and not node.right:
            if node is start_node:
                print(node.val)
                return 0
            if not is_left_branch:
                print(node.val)
                return 0
            print(node.val)
            return node.val
        # if not node.left:
        #     return traverse(node.right, False)
        # if not root.right:
        #     return traverse(node.left, True)
        return traverse(node.left, True) + traverse(node.right, False)

    return traverse(root, False)


if __name__ == '__main__':
    print(sumOfLeftLeaves(create_binary_tree_structure([4, 2, None, 3, 1, None, None, 5])))
    