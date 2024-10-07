from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for n in range(len(nums) + 1):
            indexes = list(range(n))
            while True:
                result.append([nums[i] for i in indexes])
                for i in range(n - 1, -1, -1):
                    if indexes[i] + 1 < (len(nums) if i == n - 1 else indexes[i + 1]):
                        indexes[i] += 1
                        for j in range(i + 1, n):
                            indexes[j] = indexes[j - 1] + 1
                        break
                else:
                    break
        return result


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(start, path):
            result.append(path)
            for i in range(start, len(nums)):
                helper(i + 1, path + [nums[i]])

        result = []
        helper(0, [])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([4, 3, 2, 1]))
