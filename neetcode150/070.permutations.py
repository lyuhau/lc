from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(current, rest):
            if not rest:
                result.append(current)
                return
            for i in range(len(rest)):
                helper(current + [rest[i]], rest[:i] + rest[i + 1:])

        result = []
        helper([], nums)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
