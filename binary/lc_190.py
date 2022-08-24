'''
    Leetcode 190: Reverse Bits
    https://leetcode.com/problems/reverse-bits/

    Solution: This is only possible because they gave us the guarantee
    that the numbers are 32 bits long. We essentially retrieve the bit
    from the original number by ANDing it with (1 << i). We then put this
    bit in the right place in our result by left shifting it over by (31 - 1)
    and ORing it.

    Time: O(1)
    Space: O(1)
'''

def reverseBits(n):
    """
    :type n: int
    :rtype: int
    """
    res = 0

    for i in range(32):
        bit = (n >> i) & 1
        res |= bit << (31 - i)

    return res