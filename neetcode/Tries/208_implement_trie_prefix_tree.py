class Trie:
    def __init__(self, val=None):
        self.val = val if val else ''
        self.children = [None for _ in range(26)]
        self.end = False

    def insert(self, word: str) -> None:
        if word:
            first_letter = word[0]
            pos: int = ord(first_letter) - ord('a')
            if not self.children[pos]:
                self.children[pos] = Trie(val=first_letter)
            self.children[pos].insert(word[1:])

    def search(self, word: str) -> bool:
        if word:
            pos: int = ord(word[0]) - ord('a')
            if self.children[pos]:
                if len(word) == 1 and self.children[pos]:
                    return True
                inner = self.children[pos]
                return inner.search(word[1:])
            return False
        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix:
            pos: int = ord(prefix[0]) - ord('a')
            if self.children[pos]:
                if len(prefix) == 1 and self.children[pos]:
                    return True
                inner = self.children[pos]
                return inner.search(prefix[1:])
            return False
        return False


if __name__ == '__main__':
    inputs = [
        (["insert", "search", "search", "startsWith", "insert", "search"], ["apple", "apple", "app", "app", "app", "app"]),
        # (["insert", "search", "search", "search"], ["apple", "ap", "apple", 'qw']),
    ]
    for input_ in inputs:
        trie = Trie()
        values = input_[1]
        for index, operation in enumerate(input_[0]):
            func = getattr(trie, operation)
            value = values[index]
            if operation == 'insert':
                trie.insert(value)
            elif operation == 'search':
                print(f'val = <{value}> in Trie - ' + f'{trie.search(value)}')
            elif operation == 'startsWith':
                print(trie.startsWith(value))
