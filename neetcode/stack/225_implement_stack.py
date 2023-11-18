from collections import deque


class MyStack:

    def __init__(self):
        self.elements = deque()

    def push(self, x: int) -> None:
        self.elements.append(x)

    def pop(self) -> int:
        item = self.elements.pop()
        return item

    def top(self) -> int:
        item = self.elements.pop()
        self.elements.append(item)
        return item

    def empty(self) -> bool:
        return len(self.elements) == 0


if __name__ == '__main__':
    obj = MyStack()
    obj.push(100)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()