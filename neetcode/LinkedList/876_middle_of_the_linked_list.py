from typing import Optional

from neetcode.LinkedList import ListNode, create_linked_list_structure, print_linked_list


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    nodes = {}

    current = head
    index = 0
    while current:
        nodes[index] = current
        current = current.next
        index += 1

    max_value = max(nodes.keys())

    if max_value % 2 == 0:
        ind = max_value // 2
        return nodes[ind]
    else:
        ind = max_value // 2 + 1
        return nodes[ind]


def middle_node_two_pointers_solution(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == '__main__':
    inputs = [
        [1],
        [1, 2],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
    ]
    for input_ in inputs:
        print(print_linked_list(middle_node(create_linked_list_structure(input_))))
        print(print_linked_list(middle_node_two_pointers_solution(create_linked_list_structure(input_))))
