from typing import Optional

from neetcode.LinkedList import ListNode, create_linked_list_structure


def is_palindrome_brute_force_approach(head: Optional[ListNode]) -> bool:

    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    left, right = 0, len(values) - 1
    while left <= right:
        if values[left] != values[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome(head: Optional[ListNode]) -> bool:

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next
        slow_val = slow.val if slow else 'None_Slow'
        fast_val = fast.val if fast else 'None_Fast'
        print(slow_val, fast_val)


if __name__ == '__main__':
    l_ = create_linked_list_structure([1, 2, 3, 4, 5])
    print(is_palindrome_brute_force_approach(l_))
