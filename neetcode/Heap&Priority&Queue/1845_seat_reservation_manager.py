import sys
import time
from types import ModuleType, FunctionType
from gc import get_referents

from memory_profiler import profile

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

@profile
class SeatManager:

    def __init__(self, n: int):
        self.seats = [(False, i) for i in range(0, n)]

    @profile
    def reserve(self) -> int:
        reserved_seat = None
        for i, seat in enumerate(self.seats):
            if seat[0] is False:
                reserved_seat = seat[1] + 1
                self.seats[i] = (True, i)
                break
        return reserved_seat

    def unreserve(self, seat_number: int) -> None:
        self.seats[seat_number - 1] = (False, seat_number - 1)


if __name__ == '__main__':
    # import psutil

    # process = psutil.Process()
    # while True:
    #     print(process.memory_info())
    # st = time.perf_counter()
    manager = SeatManager(10000000)
    # print(time.perf_counter() - st)
    # print(sys.getsizeof(manager))
    # manager_size = getsize(manager) / 1024 / 1024
    # print(manager_size)

    print(manager.reserve())
    print(manager.reserve())
    print(manager.unreserve(2))
    print(manager.reserve())
    print(manager.reserve())
    print(manager.reserve())
    print(manager.reserve())
    print(manager.unreserve(5))
