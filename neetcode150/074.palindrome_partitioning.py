from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(index, current):
            if index == len(s):
                result.append(current)
                return
            for i in range(index, len(s)):
                if s[index:i + 1] == s[index:i + 1][::-1]:
                    helper(i + 1, current + [s[index:i + 1]])

        result = []
        helper(0, [])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.partition('aab'))
