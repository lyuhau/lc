from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(int(b + a))
                if token == "-":
                    stack.append(int(b - a))
                if token == "*":
                    stack.append(int(b * a))
                if token == "/":
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.evalRPN(["2", "1", "+", "3", "*", "4", "-"]))
    print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
