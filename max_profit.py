from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = prices[0]
        for p in prices:
            if p < min_val:
                min_val = p
            max_profit = max(max_profit, p-min_val)
        return max_profit
