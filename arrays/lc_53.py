'''
    Leetcode 53: Maximum Subarray
    https://leetcode.com/problems/maximum-subarray/

    Solution:
    Essentially use a sliding window where we keep track of
    the current prefix sum of the subarray and see how it changes when
    we add a new element. If the prefix sum becomes negative, it is not
    contributing to the max sum and we can disregard it. We can then check
    the max of the prefix sum and our max so far

    Time: O(n) since we make one pass through the array
    Space: O(1)
'''
def maxSubArray(self, nums):
    curr = 0
    max_sub = nums[0]

    for num in nums:
        if curr < 0:
            curr = 0

        curr += num
        max_sub = max(max_sub, curr)

    return max_sub
