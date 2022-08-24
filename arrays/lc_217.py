'''
    Leetcode 217: Contains Duplicate
    https://leetcode.com/problems/contains-duplicate/

    Solution:
    Maintain a hashset of the elements. When we see a new element, check whether
    it is in the set. If it is, we can return true, and if not we can add it to the
    set.

    Time: O(n) since we scan the list once
    Space: O(n) since we use an additional set
'''

def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    duplicates = set()
    for num in nums:
        if num in duplicates:
            return True
        duplicates.add(num)
    return False