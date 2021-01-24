from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = 987654321
        max_profit = 0

        for price in prices:
            if price < min_value:
                min_value = price
            elif price - min_value > max_profit:
                max_profit = price - min_value

        return max_profit
