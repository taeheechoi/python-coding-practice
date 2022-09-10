import unittest

class Test(unittest.TestCase):

    def twoSum(self, nums, target):
        val_dict = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in val_dict:
                return [val_dict[diff], i]
            val_dict[n] = i
            

    def test_first(self):
        self.assertEqual(self.twoSum([2,7,11,15], 9), [0,1])
    
    def test_second(self):
        self.assertEqual(self.twoSum([3,2,4], 6), [1,2])

    def test_third(self):
        self.assertEqual(self.twoSum([3,3], 6), [0,1])

if __name__ == '__main__':
    unittest.main()