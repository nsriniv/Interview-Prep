'''
    Leetcode 153: Find Minimum in Rotated Sorted Array
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

    Solution:
    Since the list was sorted before being rotated, we can take advantage of this
    by performing a modified binary search. If our mid value is greater
    than our left pointer we know that the left half before the mid is sorted
    and we can search in our right half and vice versa. if we reach a portion where
    our left is smaller than our right, we know we are searching a sorted list for
    the minimum element which is just the left value. We can check this against our
    min so far and return it.

    Time: O(log n) binary search
    Space: O(1)
'''

def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] <= nums[r]:
            res = min(res, nums[l])
            break

        mid = (l + r) // 2
        res = min(res, nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1

    return res