'''
    Leetcode 338: Counting Bits
    https://leetcode.com/problems/counting-bits/

    Solution: Not an obvious solution but still nice to know. While
    our initial number, n, is not 0, we AND it with (n - 1) and increase
    our count of 1 bits. The product of this AND operation tells us whether
    n is an exact power of 2. But doing this also helps us count the rightmost
    1 bit of an integer in binary form.

    Time: O(n) since we make one pass through the array
    Space: O(1)
'''

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    res = []
    for i in range(n+1):
        count = 0
        tmp = i
        while tmp:
            tmp &= (tmp - 1)
            count += 1
        res.append(count)

    return res