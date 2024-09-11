from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M, N = len(nums1), len(nums2)
        T = (M + N) // 2 + 1

        i1, j1 = max(M - T, 0), min(T, M)
        i2, j2 = max(N - T, 0), min(T, N)

        while j1 - i1 + j2 - i2 > 6:
            c1 = (i1 + j1) // 2
            c2 = (i2 + j2) // 2
            n1, n2 = nums1[c1], nums2[c2]
            below = c1 + c2
            above = M - c1 + N - c2 - 2
            if n1 == n2:
                i1 = max(c1 - (T - above) + 1, i1)
                j1 = min(c1 + (T - below), j1)
                i2 = max(c2 - (T - above) + 1, i2)
                j2 = min(c2 + (T - below), j2)
            elif n1 < n2:
                i1 = max(c1 - (T - above) + 1, i1)
                j2 = min(c2 + (T - below) - 1, j2)
            else:
                i2 = max(c2 - (T - above) + 1, i2)
                j1 = min(c1 + (T - below) - 1, j1)

        while i1 + i2 > M - j1 + N - j2:
            if i1 > 0:
                i1 -= 1
            else:
                i2 -= 1
        while j1 + j2 < M - i1 + N - i2:
            if j1 < M:
                j1 += 1
            else:
                j2 += 1

        actual = list(sorted((*nums1[i1:j1], *nums2[i2:j2])))
        actual = (actual[len(actual) // 2] + actual[(len(actual) - 1) // 2]) / 2

        return actual


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([], [1]) == 1.0)
    print(solution.findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12]) == 6.5)
    print(solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12]) == 6.5)
    print(solution.findMedianSortedArrays([1, 2, 6], [3, 4, 5, 7, 8, 9, 10, 11, 12]) == 6.5)
    print(solution.findMedianSortedArrays([1, 2], [3]) == 2.0)
    print(solution.findMedianSortedArrays([1, 2, 4, 5], [2, 3, 4]) == 3.0)
    print(solution.findMedianSortedArrays([1, 3], [2, 4]) == 2.5)
    print(solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5)
    print(solution.findMedianSortedArrays([2, 2, 4, 4], [2, 2, 4, 4]) == 3.0)
    print(solution.findMedianSortedArrays([2, 4], [1, 3]) == 2.5)
    print(solution.findMedianSortedArrays([1, 1, 5, 5], [2, 3, 4, 5]) == 3.5)
    print(solution.findMedianSortedArrays([1, 1, 1, 1, 1, 2, 4, 4, 4, 4], [0, 0, 0, 3, 3, 3]) == 1.5)
    print(solution.findMedianSortedArrays([0, 0, 0, 0, 0, 3, 3, 3, 3, 3], [1, 1, 1, 2, 4, 4]) == 1.5)
    print(solution.findMedianSortedArrays([1, 1, 1, 1, 1, 2, 4, 4, 4, 4], [0, 0, 0, 0, 0, 3, 3, 3, 3, 3]) == 1.5)
    print(solution.findMedianSortedArrays([1, 1, 1, 1, 1, 2, 4, 4, 4, 4], [0, 0, 0, 0, 3, 3, 3, 3, 3]) == 2.0)
    print(solution.findMedianSortedArrays([1, 1, 1, 1, 2, 4, 4, 4, 4], [0, 0, 0, 0, 0, 3, 3, 3, 3, 3]) == 2.0)
    print(solution.findMedianSortedArrays([1, 1, 1, 1, 1, 2, 4, 4, 4, 4], [0, 0, 3, 3]) == 1.5)
    print(solution.findMedianSortedArrays( [0, 0, 0, 0, 0], [-1,0,0,0,0,0,1]) == 0.0)
    pass
