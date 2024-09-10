class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        seen = set()
        for i, c in enumerate(s):
            if longest > len(s) - i:
                break
            if c in seen:
                continue
            seen.add(c)

            length = 0
            left = k
            for j, l in enumerate(s):
                if l == c:
                    length += 1
                elif left > 0:
                    length += 1
                    left -= 1
                else:
                    longest = max((longest, length))
                    while s[j - length] == c:
                        length -= 1

            longest = max((longest, length))

        return longest


if __name__ == '__main__':
    solution = Solution()
    print(solution.characterReplacement("ABAB", 2))
    print(solution.characterReplacement("AAABABB", 1))
    print(solution.characterReplacement("AABABBA", 1))
    print(solution.characterReplacement("ABAA", 0))
