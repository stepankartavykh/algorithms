from typing import Optional

from neetcode.LinkedList import ListNode, create_linked_list_structure, print_linked_list


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(next_=head)
    previous, current = dummy, head

    while current:
        next_ = current.next

        if next_ and next_.val == current.val:
            previous.next = next_

        previous = next_
        current = next_

    return dummy.next


if __name__ == '__main__':
    inputs = [
        # [],
        # [1, 1, 1, 1, 1],
        [1, 1, 1],
        # [1, 1, 2],
        # [1, 1, 2, 3, 3]
    ]
    for input_ in inputs:
        print(print_linked_list(delete_duplicates(create_linked_list_structure(input_))))
