# https://leetcode.com/problems/valid-anagram/
# T: O(s+t) S: O(s+t)
import unittest

class Test(unittest.TestCase):
    def isValidAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)

        return dict_s == dict_t

    def test_first(self):
        self.assertTrue(self.isValidAnagram("anagram", "nagaram"))

    def test_second(self):
        self.assertFalse((self.isValidAnagram("rat", "car")))



if __name__ == '__main__':
    unittest.main()