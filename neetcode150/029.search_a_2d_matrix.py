from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        i = 0
        j = M * N
        while i != j:
            check = (i + j) // 2
            check_i = check // N
            check_j = check % N
            if matrix[check_i][check_j] == target:
                return True
            elif matrix[check_i][check_j] > target:
                j = check
            else:
                i = check + 1
        return False


if __name__ == '__main__':
    solution = Solution()
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=3))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=13))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=7))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=20))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=34))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=50))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=1))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=30))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=31))
    # print(solution.searchMatrix(matrix=[[1], [3]], target=1))
    # print(solution.searchMatrix(matrix=[[1], [3]], target=3))
    # print(solution.searchMatrix(matrix=[[1]], target=1))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=13))
    # print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34,