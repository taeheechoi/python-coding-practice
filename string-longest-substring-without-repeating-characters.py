import unittest

class Test(unittest.TestCase):
    def lengthOfLongestSubstring(self, s):
        l = 0
        result = 0
        charSet = set()
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
        return result



    def test_first(self):
        self.assertEqual(self.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_second(self):
        self.assertEqual(self.lengthOfLongestSubstring("bbbbb"), 1)

    def test_third(self):
        self.assertEqual(self.lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == '__main__':
    unittest.main()


    