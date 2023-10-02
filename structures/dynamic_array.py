class DynamicArray:
    
    def __init__(self, capacity: int):
        self.elements = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= len(self.elements):
            raise IndexError("Index out of range")
        return self.elements[i]

    def insert(self, i: int, n: int) -> None:
        pass

    def pushback(self, n: int) -> None:
        pass

    def popback(self) -> int:
        pass

    def resize(self) -> None:
        pass

    def getSize(self) -> int:
        pass
    
    def getCapacity(self) -> int:
        pass


if __name__ == '__main__':
    arr = DynamicArray(5)
    arr.get(0)