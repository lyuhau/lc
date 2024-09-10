from functools import cache
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(generate_parenthesis(n))

@cache
def generate_parenthesis(n):
    if n == 1:
        return {"()"}
    result = set("(" + s + ")" for s in generate_parenthesis(n-1))
    for i in range(1, n):
        left = list(generate_parenthesis(i))
        right = list(generate_parenthesis(n-i))
        for l in left:
            for r in right:
                result.add(l + r)
    return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(4))
