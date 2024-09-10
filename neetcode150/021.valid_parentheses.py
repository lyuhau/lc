class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            elif c == ")":
                if stack[-1] != "(":
                    return False
                stack.pop()
            elif c == "]":
                if stack[-1] != "[":
                    return False
                stack.pop()
            elif c == "}":
                if stack[-1] != "{":
                    return False
                stack.pop()
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("([{}])"))
