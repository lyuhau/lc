class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for c in s1:
            s1_map.setdefault(c, 0)
            s1_map[c] += 1
        s2_map = {}
        for c in s2[:len(s1)]:
            s2_map.setdefault(c, 0)
            s2_map[c] += 1

        if s1_map == s2_map:
            return True
        for i, c in list(enumerate(s2))[len(s1):]:
            s2_map.setdefault(c, 0)
            s2_map[c] += 1
            other_side = s2[i - len(s1)]
            s2_map[other_side] -= 1
            if s2_map[other_side] == 0:
                del(s2_map[other_side])
            if s1_map == s2_map:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkInclusion("abc", "lecabee"))
    print(solution.checkInclusion("abc", "lecaabee"))
