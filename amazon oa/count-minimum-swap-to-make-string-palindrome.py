# Time Complexity: O(n2) 
# Auxiliary Space: O(1)


from collections import Counter
def minSwap(s):
    s = list(s)
    count = Counter(s)
    
    result = 0
    
    left = 0
    right = len(s) -1
    
    odd = sum([c for c in count.values() if c % 2 != 0])

    if odd > 1: 
        return -1

    while left < right:
        l, r = left, right
        while s[l] != s[r]:
            r -= 1
        if l == r:
            s[r], s[r+1] = s[r+1], s[r]
            
            result += 1
            continue
        else:
            while r < right:
                s[r], s[r+1] = s[r+1], s[r]
                r += 1
                result += 1
        left += 1
        right -= 1

    return result

    






s='aabcc'
print(minSwap(s))