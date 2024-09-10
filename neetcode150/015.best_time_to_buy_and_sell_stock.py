class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        winner = 0
        bot = prices[0]
        for price in prices:
            winner = max((winner, price - bot))
            bot = min((bot, price))
        return winner


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
