from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for n in range(len(nums) + 1):
            indexes = list(range(n))
            while True:
                result.add(tuple(sorted(nums[i] for i in indexes)))
                for i in range(n - 1, -1, -1):
                    if indexes[i] + 1 < (len(nums) if i == n - 1 else indexes[i + 1]):
                        indexes[i] += 1
                        for j in range(i + 1, n):
                            indexes[j] = indexes[j - 1] + 1
                        break
                else:
                    break
        return [list(t) for t in result]


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 1, 2]))
