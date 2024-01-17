class MyHashMap:
    # TODO "hashing" is required
    def __init__(self):
        self.keys = [None for _ in range(10 ** 6 + 1)]
        self.elements = [None for _ in range(10 ** 6 + 1)]

    def put(self, key: int, value: int) -> None:
        if self.keys[key] is None:
            self.keys[key] = key
        self.elements[key] = value

    def get(self, key: int) -> int:
        if self.keys[key] is None:
            return -1
        else:
            return self.elements[key]

    def remove(self, key: int) -> None:
        if self.keys[key] is not None:
            self.keys[key] = None
            self.elements[key] = None


if __name__ == '__main__':
    test_cases = [
        (["put", "put", "get", "get", "put", "get", "remove", "get"],
         [[1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]),
        (["put", "get", "put", "get"], [[1000000, 1], [1000000], [0, 2], [0]]),
    ]
    for commands, values in test_cases:
        print('======================')
        obj = MyHashMap()
        for index, command in enumerate(commands):
            val = values[index]
            if len(val) == 2:
                key, value = val
            elif len(val) == 1:
                key = val[0]
            if command == 'put':
                obj.put(key, value)
            elif command == 'get':
                v = obj.get(key)
                print(v)
            elif command == 'remove':
                print(obj.remove(key))
            # print(obj.elements)
        print()
