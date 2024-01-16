class MyHashSet:
    def __init__(self):
        self.elements = []

    def add(self, key: int) -> None:
        if self.elements:
            left, right = 0, len(self.elements) - 1
            while left <= right:
                middle = (left + right) // 2
                if self.elements[middle] < key:
                    left = middle + 1
                elif self.elements[middle] > key:
                    right = middle - 1
                else:
                    return
            self.elements.insert(left, key)
        else:
            self.elements.append(key)

    def remove(self, key: int) -> None:
        if self.elements:
            left, right = 0, len(self.elements) - 1
            while left <= right:
                middle = (left + right) // 2
                if self.elements[middle] < key:
                    left = middle + 1
                elif self.elements[middle] > key:
                    right = middle - 1
                else:
                    del self.elements[middle]
                    return

    def contains(self, key: int) -> bool:
        left, right = 0, len(self.elements) - 1
        while left <= right:
            position = (left + right) // 2
            if key > self.elements[position]:
                left = position + 1
            elif key < self.elements[position]:
                right = position - 1
            else:
                return True
        return False


if __name__ == '__main__':
    test_cases = [
        # ("MyHashSet", "add", "remove", "add", "remove", "remove", "add", "add", "add", "add", "remove"),
        ("MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains")
    ]
    values_sets = [
        # ([], [9], [19], [14], [19], [9], [0], [3], [4], [0], [9]),
        ([], [1], [2], [1], [3], [2], [2], [2], [2]),
    ]
    for num_test_case, test_case in enumerate(test_cases):
        print('======================')
        obj = MyHashSet()
        for index, command in enumerate(test_case):
            val = values_sets[num_test_case][index]
            if command == 'add':
                obj.add(val)
            elif command == 'remove':
                obj.remove(val)
            elif command == 'contains':
                print(obj.contains(val))
            print(obj.elements)
        print()
