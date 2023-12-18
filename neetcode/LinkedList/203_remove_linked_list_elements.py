from typing import Optional

from neetcode.LinkedList import ListNode, create_linked_list_structure, print_linked_list


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    pointer_to_head = ListNode(next_=head)
    previous = pointer_to_head
    current = head

    while current:
        if current.val == val:
            previous.next = current.next
        else:
            previous = current
        current = current.next
    return pointer_to_head.next


if __name__ == '__main__':
    input_structures = [
        ([1, 2, 6, 3, 4, 5, 6], 6),
        ([], 1),
        ([7, 7, 7, 7], 7),
    ]
    for struct in input_structures:
        linked_list = create_linked_list_structure(struct[0])
        print(print_linked_list(remove_elements(linked_list, struct[1])))
        print('----')
