from typing import Optional


class Node:
    def __init__(self, x: int, next_=None, random=None):
        self.val = int(x)
        self.next = next_
        self.random = random


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    # TODO Resolve later!
    # Initialise hashmap (with None in order to 'move' pointer to None)
    old_to_copy = {None: None}
    # Make two passes: one for creating hashmap (create deep copy of each node), second for linking pointers in
    # copied linked list
    current = head
    while current:
        copy = Node(current.val)
        old_to_copy[current] = copy
        current = current.next
    current = head
    while current:
        copy = old_to_copy[current]
        copy.next = old_to_copy[current.next]
        copy.random = old_to_copy[current.random]
        current = current.next

    return old_to_copy[head]

