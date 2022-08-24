'''
    Leetcode 191: Number of 1 Bits
    https://leetcode.com/problems/number-of-1-bits/

    Solution: Not an obvious solution but still nice to know. While
    our initial number, n, is not 0, we AND it with (n - 1) and increase
    our count of 1 bits. The product of this AND operation tells us whether
    n is an exact power of 2. But doing this also helps us count the rightmost
    1 bit of an integer in binary form.

    Time: O(1)
    Space: O(1)
'''

def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    res = 0
    while n:
        n &= (n-1)
        res += 1

    return res