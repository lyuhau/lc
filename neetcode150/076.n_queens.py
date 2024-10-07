from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def can_place(row, col, queens):
            for r, c in enumerate(queens):
                if c == col or r == row or abs(row - r) == abs(col - c):
                    return False
            return True

        def helper(row, queens):
            if row == n:
                result.append([''.join('Q' if c == col else '.' for col in range(n)) for r, c in enumerate(queens)])
                return
            for col in range(n):
                if can_place(row, col, queens):
                    helper(row + 1, queens + [col])

        result = []
        helper(0, [])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
