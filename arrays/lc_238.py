'''
    Leetcode 238: Product of Array Except Self
    https://leetcode.com/problems/product-of-array-except-self/

    Solution:
    Make two passes over the input array. In the first, we calculate
    the prefix product of every element and store it in the output
    array. In the second, we multiply the prefix product with the postfix
    product of every element. The prefix * postfix is the product of
    every element except for itself.

    Time: O(n) since we have two passes that are each O(n)
    Space: O(1) since we don't count the space of the output array
'''

def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in  range(len(nums) - 1, -1, -1):
        res[i] *= prefix
        postfix *= nums[i]

    return res

