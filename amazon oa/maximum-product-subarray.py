# https://leetcode.com/problems/maximum-product-subarray/
# https://codeforces.com/blog/entry/94518
# 31. Find Max products Amazon OA 2022 Solution

def maxProduct(nums):
    res = nums[0]
    curMin, curMax = 1, 1

    for n in nums:
        tmp = curMax * n
        curMax = max(n*curMax, n*curMin, n)
        curMin = min(tmp, n*curMin, n)
        res = max(res, curMax)
    return res


