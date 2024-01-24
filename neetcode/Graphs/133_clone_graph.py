from typing import Optional

from neetcode.Graphs import Node


def func(node: Optional[Node]):
    if not node:
        return []
    return node.val


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    copy_node = Node(node.val)

    visited_nodes = set()

    def traverse_graph(current_node, where_to_add):
        if id(current_node) in visited_nodes:
            return
        for adjacent_node in current_node.neighbors:
            where_to_add.neighbors.append(adjacent_node)
            visited_nodes.add(id(current_node))
            traverse_graph(adjacent_node, current_node)

    traverse_graph(node, copy_node)

    return copy_node


if __name__ == '__main__':
    # input_edges = [[2, 4], [1, 3], [2, 4], [1, 3]]

    print(func(Node()))
    print(func(None))
