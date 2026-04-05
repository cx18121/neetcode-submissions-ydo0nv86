class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        ret = 0
        for i in range(1, len(prices)):
            m = min(m, prices[i])
            ret = max(ret, prices[i] - m)
        return ret