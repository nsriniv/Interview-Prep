'''
    Leetcode 33: Search in Rotated Sorted Array
    https://leetcode.com/problems/search-in-rotated-sorted-array/

    Solution:
    Since the list was sorted before being rotated, we can take advantage of this
    by performing a modified binary search. If our mid value is equal to our target
    we can return it. Otherwise we have 6 basic cases that we have to consider.
    Case 1: Mid >= Left
        Case 1a: Target > Mid
            If our target is larger than where we are looking, then we look at the right
            subarray
        Case 1b: Target < Left
            If our target is smaller than our left, then we also look at the right subarray
        Case 1c: Otherwise we look at the left subarray
    Case 2: Otherwise
        Case 2a: Target < Mid
            If our target is smaller than where we are looking, then we look at the left
            subarray
        Case 2b: Target > Right
            If our target is larger than our right, then we also look at the left subarray
        Case 2c: Otherwise we look at the right subarray

    Time: O(log n) binary search
    Space: O(1)
'''

def search(nums, target):

    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1