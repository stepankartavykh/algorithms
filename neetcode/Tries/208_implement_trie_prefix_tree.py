class Trie:
    def __init__(self, val=None):
        self.val = ''
        self.children = [None for _ in range(26)]
        self.end = False

    def insert(self, word: str) -> None:
        first_letter = word[0]
        pos = ord(first_letter) - ord('a')
        self.children[pos] = Trie()

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass
