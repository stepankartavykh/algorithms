from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def print_linked_list(node):
    if node is None:
        return
    print(node.val)
    print_linked_list(node.next)


# TODO make comparison between solutions. Which one is better?
def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    start_merged = ListNode()
    current = start_merged

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    return start_merged.next


def second_recursion_approach_merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 == None and list2 == None:
        return None
    elif list1 == None:
        return list2
    elif list2 == None:
        return list1

    if list1.val <= list2.val:
        return ListNode(list1.val, second_recursion_approach_merge_two_lists(list1.next, list2))
    return ListNode(list2.val, second_recursion_approach_merge_two_lists(list2.next, list1))
