class MyHashSet:
    #  TODO binary search must be implemented
    def __init__(self):
        self.elements = []

    def add(self, key: int) -> None:
        if key not in self.elements:
            self.elements.append(key)

    def remove(self, key: int) -> None:
        for index in range(len(self.elements)):
            if self.elements[index] == key:
                del self.elements[index]
                break

    def contains(self, key: int) -> bool:
        return True if key in self.elements else False


if __name__ == '__main__':
    commands = ["MyHashSet", "add", "remove", "add", "remove", "remove", "add", "add", "add", "add", "remove"]
    values = [[], [9], [19], [14], [19], [9], [0], [3], [4], [0], [9]]
    obj = MyHashSet()
    for index, command in enumerate(commands):
        if command == 'add':
            obj.add(values[index][0])
        elif command == 'remove':
            obj.remove(values[index][0])
