class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = float('inf')
        maximum = 0

        for day,price in enumerate(prices):
            if price < minimum:
                minimum = price
            else:
                maximum = max(maximum,price-minimum)
        
        return maximum