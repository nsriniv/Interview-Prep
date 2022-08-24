'''
    Leetcode 268: Missing Number
    https://leetcode.com/problems/missing-number/

    Solution: Return the difference between the sum of the range
    and the sum of the array. Sum of the range can be calculated using
    Gauss' formula.

    Time: O(n) since we make one pass through the array for the sum
    Space: O(1)
'''

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    arr_sum = sum(nums)
    expected = len(nums) * (len(nums) + 1) / 2

    return expected - arr_sum