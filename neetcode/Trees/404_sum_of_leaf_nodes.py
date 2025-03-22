from neetcode.Trees import TreeNode, create_binary_tree_structure



def sumOfLeftLeaves(root: TreeNode | None) -> int:

    res = 0

    def traverse(node):
        nonlocal res

        if not node:
            return
        if node.left and not node.left.left and not node.left.right:
            res += node.left.val
        
        traverse(node.left)
        traverse(node.right)
        
    traverse(root)
    
    return res


if __name__ == '__main__':
    print(sumOfLeftLeaves(create_binary_tree_structure([4, 2, None, 3, 1, None, None, 5])))
    