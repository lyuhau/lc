from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        combinations = []
        for digit in digits:
            combinations = [
                combination + letter
                for combination in combinations or [""]
                for letter in mapping[digit]
            ]
        return combinations


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
