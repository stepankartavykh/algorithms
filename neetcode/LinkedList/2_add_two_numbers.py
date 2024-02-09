from neetcode.LinkedList import ListNode, create_linked_list_structure, print_linked_list


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    l1_current = l1
    l2_current = l2
    sum_head = ListNode()
    sum_current = sum_head
    is_plus_one = False
    while l1_current and l2_current:
        s = l1_current.val + l2_current.val + is_plus_one
        if s > 9:
            sum_current.val = s % 10
            is_plus_one = True
        else:
            sum_current.val = s
            is_plus_one = False

        l1_current = l1_current.next
        l2_current = l2_current.next
        if l1_current and l2_current:
            sum_current.next = ListNode()
            sum_current = sum_current.next

    if not l1_current and not l2_current:
        if not is_plus_one:
            return sum_head
        sum_current.next = ListNode(val=1)
        return sum_head

    while l1_current:
        sum_current.next = ListNode()
        sum_current = sum_current.next
        s = l1_current.val + is_plus_one
        if s > 9:
            is_plus_one = True
            sum_current.val = s % 10
        else:
            is_plus_one = False
            sum_current.val = s
        l1_current = l1_current.next
    while l2_current:
        sum_current.next = ListNode()
        sum_current = sum_current.next
        s = l2_current.val + is_plus_one
        if s > 9:
            is_plus_one = True
            sum_current.val = s % 10
        else:
            is_plus_one = False
            sum_current.val = s
        l2_current = l2_current.next
    if is_plus_one:
        sum_current.next = ListNode(val=1)
    return sum_head


def add_two_numbers_second_solution(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    # TODO Nice solution. Rewrite later again!
    empty_start = ListNode()
    current = empty_start

    is_plus_one = 0
    while l1 or l2 or is_plus_one:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        new_digit = v1 + v2 + is_plus_one
        is_plus_one = new_digit // 10
        new_digit %= 10
        current.next = ListNode(val=new_digit)

        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return empty_start.next


if __name__ == '__main__':
    inputs = [
        ([0], [0]),
        ([2, 4, 3], [5, 6, 4]),
        ([2, 4, 3], [5, 6, 7]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),
    ]
    for input_ in inputs:
        print(print_linked_list(add_two_numbers(
            create_linked_list_structure(input_[0]),
            create_linked_list_structure(input_[1])
        )))
