import sys
import time
from types import ModuleType, FunctionType
from gc import get_referents


BLACKLIST = type, ModuleType, FunctionType


def getsize(obj):
    """sum size of object & members."""
    if isinstance(obj, BLACKLIST):
        raise TypeError('getsize() does not take argument of type: '+ str(type(obj)))
    seen_ids = set()
    size = 0
    objects = [obj]
    while objects:
        need_referents = []
        for obj in objects:
            if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)
    return size

"""
Design a system that manages the reservation state of n seats that are numbered from 1 to n.
Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
"""



class SeatManager:

    def __init__(self, n: int):
        self.count = n
        self.seats = {
            i: False
            for i in range(1, n + 1)
        }
        self.last_free = 1

    def reserve(self) -> int:
        self.seats[self.last_free] = True
        number_to_return = self.last_free
        for i in range(self.last_free, self.count + 1):
            if self.seats[i] is False:
                self.last_free = i
                break
        return number_to_return

    def unreserve(self, seat_number: int) -> None:
        if seat_number < self.last_free:
            self.last_free = seat_number
        self.seats[seat_number] = False


if __name__ == '__main__':
    manager = SeatManager(5)
    print(manager.reserve())
    print(manager.reserve())
    print(manager.unreserve(2))
    print(manager.reserve())
    print(manager.reserve())
    print(manager.reserve())
    print(manager.reserve())
    print(manager.unreserve(5))

    manager_second = SeatManager(2)
    print(manager_second.reserve())
    print(manager_second.unreserve(1))
    print(manager_second.reserve())
    print(manager_second.reserve())
    print(manager_second.unreserve(2))
    print(manager_second.reserve())
    print(manager_second.unreserve(1))
    print(manager_second.reserve())
    print(manager_second.unreserve(2))
    print(manager_second.reserve())