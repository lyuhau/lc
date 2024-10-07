from collections import defaultdict


class PrefixTree:
    def __init__(self):
        def defaultdict_factory():
            return defaultdict(defaultdict_factory)
        self.trie = defaultdict_factory()

    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            node = node[char]
        node['#'] = '#'

    def search(self, word: str) -> bool:
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


if __name__ == '__main__':
    s = PrefixTree()
    s.insert('apple')
    print(s.search('apple'))
    print(s.startsWith('app'))
    print(s.startsWith('aps'))
