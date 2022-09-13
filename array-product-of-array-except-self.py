import unittest


class Test(unittest.TestCase):

    def productExceptSelf(self, nums):
        prefix = 1
        result = [1]*len(nums)
        
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
       
    def test_first(self):
        self.assertEqual(self.productExceptSelf([1,2,3,4]), [24,12,8,6])

    def test_second(self):
        self.assertEqual(self.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])

if __name__ == '__main__':
    unittest.main()
