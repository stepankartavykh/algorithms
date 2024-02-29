import collections

from neetcode.Trees import TreeNode, create_binary_tree_structure


def isEvenOddTree(root: TreeNode | None) -> bool:
    # TODO Refactor this!
    level = 0
    deque = collections.deque([root])

    while deque:
        nodes = []
        while deque:
            nodes.append(deque.popleft())
        if level % 2 == 0:
            for index in range(len(nodes)):
                if nodes[index].val % 2 == 0:
                    return False
            for index in range(len(nodes) - 1):
                if nodes[index].val >= nodes[index + 1].val:
                    return False
        else:
            for index in range(len(nodes)):
                if nodes[index].val % 2 == 1:
                    return False
            for index in range(len(nodes) - 1):
                if nodes[index].val <= nodes[index + 1].val:
                    return False

        for node in nodes:
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        level += 1

    return True


if __name__ == '__main__':
    trees = [
        [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2],
        [5, 4, 2, 3, 3, 7],
    ]
    for tree in trees:
        print(isEvenOddTree(create_binary_tree_structure(tree)))
