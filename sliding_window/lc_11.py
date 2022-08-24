'''
    Leetcode 33: Container With Most Water
    https://leetcode.com/problems/container-with-most-water/

    Solution:
    Maintain a left and right pointer that are initialized to the beginning and end
    of the array. Calculate the area of the container with the min of left and right as
    height and the delta as width. If this is maximal, update our max. Update our pointers
    based on whichever is the bottleneck.

    Time: O(n) cause we do one pass over the array
    Space: O(1)
'''

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        max_area = max(max_area, area)

        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1

    return max_area