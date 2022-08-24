'''
    Leetcode 121: Best Time to Buy and Sell Stock
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    Solution:
    Use a two pointer approach where we check the delta between the
    pointers and maximize it against our max so far. If the right pointer is
    lower than the left, we can set left to right. Regardless, we continue
    scanning the list by incrementing right.

    Time: O(n) since we scan the list once
    Space: O(1)
'''

def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                diff = prices[right] - prices[left]
                max_profit = max(max_profit, diff)
            elif prices[right] < prices[left]:
                left = right
            right += 1

        return max_profit