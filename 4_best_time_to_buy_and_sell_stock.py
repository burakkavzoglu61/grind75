from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        if len(prices)==0:
            return result
        min = prices[0]
        for elem in prices:
            diff = elem - min
            if elem<min:
                min = elem
            if diff>result:
                result = diff

        return result