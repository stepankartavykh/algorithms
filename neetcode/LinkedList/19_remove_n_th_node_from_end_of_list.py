from typing import Optional

from neetcode.LinkedList import ListNode, create_linked_list_structure, print_linked_list


def remove_n_th_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # TODO rewrite this! Edge cases processing is horrible!
    first_left = None
    second_left = head

    index = 0
    last = head
    while last.next:
        # TODO how to process better?
        if index >= n - 1:
            first_left = second_left
            second_left = second_left.next
        last = last.next
        index += 1

    # TODO index and n relation in terms of TODO above?
    next_second = second_left.next
    if not next_second and first_left:
        first_left.next = None
        return head
    elif index < n:
        return next_second
    elif not next_second:
        return None
    first_left.next = next_second

    return head


if __name__ == '__main__':
    inputs = [
        ([1, 2, 3, 4, 5], 2),
        ([1], 1),
        ([1, 2], 1),
        ([1, 2, 3], 1),
        ([1, 2, 3, 4, 5, 6], 1),
        ([1, 2], 2),
        ([1, 2, 3], 3),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3),
    ]
    for input_ in inputs:
        list_without_element = remove_n_th_from_end(create_linked_list_structure(input_[0]), input_[1])
        print(print_linked_list(list_without_element))
