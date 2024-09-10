class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        for c in t:
            t_map.setdefault(c, 0)
            t_map[c] += 1

        shortest = ""

        needed_letters = set(t_map.keys())
        length = 0
        for i, c in enumerate(s):
            length += 1
            if c in t_map:
                t_map[c] -= 1
                if t_map[c] == 0:
                    needed_letters.remove(c)
                    while not needed_letters:
                        to_remove = s[i-length+1]
                        if to_remove in t_map:
                            t_map[to_remove] += 1
                            if t_map[to_remove] > 0:
                                if not shortest or length < len(shortest):
                                    shortest = s[i-length+1:i+1]
                                needed_letters.add(to_remove)
                        length -= 1
        return shortest


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))
    print(solution.minWindow("OUZODYXAZV", "XYZ"))
