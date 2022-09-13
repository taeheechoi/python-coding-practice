import unittest

class Test(unittest.TestCase):
    def maxSubArray(self, nums):
        result = nums[0]
        
        total = 0
        for num in nums:
            total += num
            result = max(result, total)
            if total < 0:
                total = 0
        
        return result

    def test_first(self):
        self.assertEqual(self.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)

    def test_second(self):
        self.assertEqual(self.maxSubArray([1]), 1)

    def test_third(self):
        self.assertEqual(self.maxSubArray([5,4,-1,7,8]), 23)

if __name__ == '__main__':
    unittest.main()