from collections import defaultdict

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class defaultdict_factory():
            def __call__(self):
                return defaultdict(dd_fact)
            def __repr__(self):
                return "dd_fact"
        dd_fact = defaultdict_factory()

        trie = dd_fact()
        for word in words:
            node = trie
            for char in word:
                node = node[char]
            node["#"] = "#"

        def dfs(i, j, node, path):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node or board[i][j] == "#":
                return
            tmp, board[i][j] = board[i][j], "#"
            node = node[tmp]
            path += tmp
            if "#" in node:
                result.add(path)
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + x, j + y, node, path)
            board[i][j] = tmp

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie, "")
        return list(result)


if __name__ == '__main__':
    s = Solution()
    print(s.findWords([
        ["a", "b", "c", "d"],
        ["s", "a", "a", "t"],
        ["a", "c", "k", "e"],
        ["a", "c", "d", "n"],
    ], ["back", "bat", "cat", "backend"]))
    print(s.findWords([
        ["a"],
    ], ["a"]))
