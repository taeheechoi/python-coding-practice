import unittest

class Test(unittest.TestCase):
    def lengthOfLongestSubstring(self, s):
        l = 0 
        result = 0
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            result = max(result, r-l + 1)
        return result


    def test_first(self):
        self.assertEqual(self.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_second(self):
        self.assertEqual(self.lengthOfLongestSubstring("bbbbb"), 1)

    def test_third(self):
        self.assertEqual(self.lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == '__main__':
    unittest.main()


    