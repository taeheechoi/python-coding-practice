# https://leetcode.com/problems/search-in-rotated-sorted-array/
# T: O(log n) S: O(1)
import unittest

class Test(unittest.TestCase):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return - 1




    def test_first(self):
        self.assertEqual(self.search([4,5,6,7,0,1,2], 0), 4)

    
    def test_second(self):
        self.assertEqual(self.search([4,5,6,7,0,1,2], 3), -1)

    def test_third(self):
        self.assertEqual(self.search([1], 0), -1)


if __name__ == '__main__':
    unittest.main()