# https://leetcode.com/problems/valid-palindrome/
# T: O(n) S: O(1) the amount of memory that you use is constant and does not depends on the data that it is processing
import unittest

class Test(unittest.TestCase):

    def isPalindrome(self, s):
        l, r = 0, len(s) -1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


    def test_first(self):
        self.assertTrue(self.isPalindrome("A man, a plan, a canal: Panama"))

    def test_second(self):
        self.assertFalse(self.isPalindrome( "race a car"))
    
    def test_third(self):
        self.assertTrue(self.isPalindrome("  "))





if __name__ == '__main__':
    unittest.main()