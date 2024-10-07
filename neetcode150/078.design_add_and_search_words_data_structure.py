from collections import defaultdict


class WordDictionary:
    def __init__(self):
        def defaultdict_factory():
            return defaultdict(defaultdict_factory)
        self.trie = defaultdict_factory()

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            node = node[char]
        node['#'] = '#'

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return '#' in node
            if word[i] == '.':
                return any(dfs(i + 1, node[char]) for char in node if char != '#')
            if word[i] in node:
                return dfs(i + 1, node[word[i]])
            return False

        return dfs(0, self.trie)


if __name__ == '__main__':
    s = WordDictionary()
    s.addWord('bad')
    s.addWord('dad')
    s.addWord('mad')
    print(s.search('pad'))
    print(s.search('bad'))
    print(s.search('.ad'))
    print(s.search('b.d'))
    print(s.search('ba.'))
    print(s.search('.'))
    print(s.search('..'))
    print(s.search('...'))
    print(s.search('....'))
