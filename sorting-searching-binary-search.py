import unittest

class Test(unittest.TestCase):

    def binarySearch(self, nums, target):
        l, r = 0, len(nums) -1
        
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1 
        
        return -1

    def test_first(self):
        self.assertEqual(self.binarySearch([-1,0,3,5,9,12], 9), 4)

    def test_second(self):
        self.assertEqual(self.binarySearch( [-1,0,3,5,9,12], 2), -1)

if __name__ == '__main__':
    unittest.main()
