'''
    Leetcode 152: Maximum Product Subarray
    https://leetcode.com/problems/maximum-product-subarray/

    Solution: Dynamic programming where we keep track and compute two values:
    The current max product and the current min product. We do this because when
    we encounter a negative value when we multiply curr_min * -ve value, we get
    a maximum. Then in every pass, we can recompute our curr max and min with
    multiplying it with the new value and seeing the maximum of the results compared
    to the value itself.

    Time: O(n) since we make one pass through the array
    Space: O(1)
'''

def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = max(nums)
    curr_max, curr_min = 1, 1

    for num in nums:
        if num == 0:
            curr_max, curr_min = 1, 1
            continue

        tmp = curr_max * num
        curr_max = max(tmp, curr_min * num, num)
        curr_min = min(tmp, curr_min * num, num)

        res = max(res, curr_max)

    return res