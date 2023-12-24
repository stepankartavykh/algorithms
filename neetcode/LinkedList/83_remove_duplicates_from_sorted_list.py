from typing import Optional

from neetcode.LinkedList import ListNode, create_linked_list_structure, print_linked_list


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(next_=head)
    previous, current = dummy, head

    while current and current.next:
        nxt = current.next

        if nxt.val == current.val:
            previous.next = nxt
        else:
            previous = current
        current = nxt

    return dummy.next


if __name__ == '__main__':
    inputs = [
        [],
        [1, 1],
        [3, 3, 3, 3],
        [1, 2, 2, 4, 5, 6],
        [1, 1, 2],
        [1, 1, 2, 3, 3]
    ]
    for input_ in inputs:
        print(print_linked_list(delete_duplicates(create_linked_list_structure(input_))))
