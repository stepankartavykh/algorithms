from neetcode import TreeNode, create_binary_tree_structure


def sum_numbers(root: TreeNode | None) -> int:
    def dfs(node, current_num):
        if not node:
            return
        current_num = current_num * 10 + node.val
        if not node.left and not node.right:
            return current_num
        return dfs(node.left, current_num) + dfs(node.right, current_num)

    return dfs(root, 0)


if __name__ == '__main__':
    print(sum_numbers(create_binary_tree_structure([0, 1])))
    print(sum_numbers(create_binary_tree_structure([1, 1, 1])))
    print(sum_numbers(create_binary_tree_structure([1, 2, 3])))
    print(sum_numbers(create_binary_tree_structure([4, 9, 0, 5, 1])))
