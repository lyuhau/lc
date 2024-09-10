class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        inside = set()
        longest = 0
        for i, c in enumerate(s):
            while c in inside:
                inside.remove(s[i - len(inside)])
            inside.add(c)
            longest = max((longest, len(inside)))
        return longest


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))
    print(solution.lengthOfLongestSubstring("zxyzxyz"))
    print(solution.lengthOfLongestSubstring("xxxx"))