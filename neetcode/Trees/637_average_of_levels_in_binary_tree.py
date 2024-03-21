from neetcode import TreeNode, create_binary_tree_structure


def averageOfLevels(root: TreeNode | None) -> list[float]:
    levels = [root.val]

    deq = [root]

    while deq:

        current_level = []
        current_level_total = 0
        for node in deq:
            if node.left:
                current_level.append(node.left)
                current_level_total += node.left.val
            if node.right:
                current_level.append(node.right)
                current_level_total += node.right.val
        if current_level:
            levels.append(current_level_total / len(current_level))
        deq = current_level

    return levels


if __name__ == '__main__':
    print(averageOfLevels(create_binary_tree_structure([3, 9, 20, None, None, 15, 7])))
