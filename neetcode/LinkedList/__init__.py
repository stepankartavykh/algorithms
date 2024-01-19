from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __repr__(self):
        return '<ListNode(val={val})>'.format(val=self.val)


def print_linked_list(node):
    result = []
    current = node
    while current:
        result.append(current.val)
        current = current.next
    return result


def create_linked_list_structure(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None

    head = ListNode()
    current = head
    for index in range(len(values) - 1):
        current.val = values[index]
        current.next = ListNode()
        current = current.next
    current.val = values[-1]
    return head
