import collections


class MinStack:

    def __init__(self):
        self.elements = collections.deque()
        self.min_position = None

    def push(self, val: int) -> None:
        self.elements.append(val)
        if self.min:
            if val < self.elements[self.min_position]:
                self.min_position = len(self.elements)

    def pop(self) -> None:
        if self.min_position == len(self.elements):
            self.elements.pop()
            for elem in self.elements:
                if
        else:
            self.elements.pop()

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.elements


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    print(minStack.elements, minStack.min)
    minStack.push(0)
    print(minStack.elements, minStack.min)
    minStack.push(-3)
    print(minStack.elements, minStack.min)
    minStack.getMin()
    print(minStack.elements, minStack.min)
    minStack.pop()
    print(minStack.elements, minStack.min)
    minStack.top()
    print(minStack.elements, minStack.min)
    minStack.getMin()
    print(minStack.elements, minStack.min)
