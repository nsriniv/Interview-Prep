'''
    Leetcode 1: Two Sum
    https://leetcode.com/problems/two-sum/

    Solution:
    Maintain a hashmap that stores each element with their index. When
    we encounter an element in the list, we can check whether its complement
    exists in our hashmap. If it does, we can return the index of the element
    and its complement (stored as the value in the hashmap)

    Time: O(n) since we scan the list once
    Space: O(n) since we use an additional hashmap
'''

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, val in enumerate(nums):
        complement = target - val
        if complement in d:
            return [d[complement], i]

        d[val] = i