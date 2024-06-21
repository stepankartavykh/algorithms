class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for symbol in word:
            i = ord(symbol) - ord('a')
            if current.children[i] is None:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.end = True

    def search(self, word: str) -> bool:
        current = self.root
        for symbol in word:
            i = ord(symbol) - ord('a')
            if current.children[i] is None:
                return False
            current = current.children[i]
        return current.end

    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for symbol in prefix:
            i = ord(symbol) - ord('a')
            if current.children[i] is None:
                return False
            current = current.children[i]
        current.end = True


class TrieConciseApproach:

    def __init__(self):
        self.trie = {}
        self.words = set()

    def insert(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        self.words.add(word)

    def search(self, word: str) -> bool:
        return word in self.words

    def starts_with(self, prefix: str) -> bool:
        cur = self.trie
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True


if __name__ == '__main__':
    inputs = [
        (["insert", "search", "search", "startsWith", "insert", "search"], ["apple", "apple", "app", "app", "app", "app"]),
        (["insert", "search", "search", "search"], ["apple", "ap", "apple", 'qw']),
    ]
    for input_ in inputs:
        trie = TrieConciseApproach()
        values = input_[1]
        for index, operation in enumerate(input_[0]):
            value = values[index]
            if operation == 'insert':
                trie.insert(value)
            elif operation == 'search':
                print(f'val = <{value}> in Trie - ' + f'{trie.search(value)}')
            elif operation == 'startsWith':
                print(trie.starts_with(value))
