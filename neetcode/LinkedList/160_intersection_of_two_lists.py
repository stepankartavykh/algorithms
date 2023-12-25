from typing import Optional

from neetcode.LinkedList import ListNode


def get_intersection_node(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    hashmapA = set()
    hashmapB = set()
    current_A = headA
    current_B = headB

    while current_A or current_B:
        if current_A:
            id_A = id(current_A)
            if id_A in hashmapB:
                return current_A
            hashmapA.add(id_A)
        if current_B:
            id_B = id(current_B)
            if id_B in hashmapA:
                return current_B
            hashmapB.add(id_B)

        current_A = current_A.next if current_A else None
        current_B = current_B.next if current_B else None

    return None
