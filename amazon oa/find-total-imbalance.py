# https://leetcode.com/problems/sum-of-subarray-ranges/
# https://leetcode.com/problems/sum-of-subarray-ranges/discuss/2499782/Simple-Python-Solution

def subArrayRanges(nums):
    minSum, maxSum = 0,0
    stack,n = [],len(nums)
    for nextSmaller in range(n+1):
        while stack and (nextSmaller == n or nums[stack[-1]] > nums[nextSmaller]):
            i = stack.pop()
            prevSmaller = -1 if stack == [] else stack[-1]
            minSum += nums[i]*(nextSmaller-i)*(i-prevSmaller)
        stack.append(nextSmaller)
    stack = []
    for nextGreater in range(n+1):
        while stack and (nextGreater == n or nums[stack[-1]] < nums[nextGreater]):
            i = stack.pop()
            prevGreater = -1 if stack == [] else stack[-1]
            maxSum += nums[i]*(nextGreater-i)*(i-prevGreater)
        stack.append(nextGreater)
    return maxSum-minSum


nums = [1,2,3]
print(subArrayRanges(nums))