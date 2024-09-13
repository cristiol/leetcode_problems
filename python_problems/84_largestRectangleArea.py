"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""


def largestRectangleArea(heights):

    max_area = 0
    stk = []

    for i, h in enumerate(heights):
        start = i
        while stk and stk[-1][1] > h:
            index, height = stk.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stk.append((start, h))

    for i, h in stk:
        max_area = max(max_area, h * (len(heights) - i))

    return max_area


print(largestRectangleArea([2,1,5,6,2,3]))
