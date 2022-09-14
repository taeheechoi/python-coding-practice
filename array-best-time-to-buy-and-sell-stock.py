# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# T: O(n) S: O(1)
import unittest

class Test(unittest.TestCase):

    def maxProfit(self, prices):
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit
             

    def test_first(self):
        self.assertEqual(self.maxProfit([7,1,5,3,6,4]), 5)
    
    def test_second(self):
        self.assertEqual(self.maxProfit([7,6,4,3,1]), 0)

    

if __name__ == '__main__':
    unittest.main()