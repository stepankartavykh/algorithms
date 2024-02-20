from typing import Optional

from neetcode.Graphs import Node


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    # TODO Resolve it later!
    old_to_new_hashmap = {}

    def clone(current_node):
        if current_node in old_to_new_hashmap:
            return old_to_new_hashmap[current_node]

        current_node_clone = Node(current_node.val)
        old_to_new_hashmap[current_node] = current_node_clone

        for neighbour in current_node.neighbors:
            neighbour_cloned_version = clone(neighbour)
            current_node_clone.neighbors.append(neighbour_cloned_version)
        return current_node_clone

    return clone(node) if node else None


if __name__ == '__main__':
    pass
