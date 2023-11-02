from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __repr__(self):
        return f"{self.val}"

    def insert_at_end(self, data):
        new_node = ListNode(data)
        if self.next is None:
            self.next = new_node
            return
        current_node = self.next
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node


def print_linked_list(node):
    if node is None:
        return
    print(node.val)
    print_linked_list(node.next)


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    previous, current = None, head

    while current:
        var = current.next
        current.next = previous
        previous = current
        current = var
    return previous


if __name__ == '__main__':
    h = ListNode()
    for i in range(1, 5):
        h.insert_at_end(i)
    # print_linked_list(h)
    print(print_linked_list(reverse_list(h)))
