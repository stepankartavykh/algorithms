class MinStack:

    def __init__(self):
        self.elements = []
        self.top_ = None
        self.min_value = None

    def push(self, val: int) -> None:
        if self.min_value is None:
            self.elements.append((val, val))
            self.top_ = (val, val)
            self.min_value = val
        else:
            self.min_value = min(val, self.min_value)
            self.top_ = (val, self.min_value)
            self.elements.append(self.top_)

    def pop(self) -> None:
        self.elements.pop()
        if len(self.elements):
            self.top_ = self.elements[-1]
            self.min_value = self.top_[1]
        else:
            self.elements = []
            self.top_ = None
            self.min_value = None

    def top(self) -> int:
        return self.top_[0]

    def getMin(self) -> int:
        return self.min_value


if __name__ == '__main__':
    inputs = [
        (["push", "push", "push"], [0, 1, 0]),
        (["push", "push", "push", "getMin", "pop", "top", "getMin"], [-2, 0, -3, None, None, None, None]),
        (["push", "push", "push", "getMin", "pop", "getMin"], [0, 1, 0, None, None, None]),
    ]
    for input_ in inputs:
        stack = MinStack()
        values = input_[1]
        for index, operation in enumerate(input_[0]):
            func = getattr(stack, operation)
            value = values[index]
            if operation == 'push':
                print(func(value), stack.elements)
            else:
                print(func(), stack.elements)
