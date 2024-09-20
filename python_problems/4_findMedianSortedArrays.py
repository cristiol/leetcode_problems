"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""



def findMedianSortedArrays(nums1, nums2):
    a, b = nums1, nums2
    total = len(a) + len(b)
    half = total // 2

    if len(b) < len(a):
        a, b = b, a

    l, r = 0, len(a) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2

        a_left = a[i] if i >= 0 else float('-inf')
        a_right = a[i + 1] if (i + 1) < len(a) else float('inf')
        b_left = b[j] if j >= 0 else float('-inf')
        b_right = b[j + 1] if (j + 1) < len(b) else float("inf")

        # partition is corect
        if a_left <= b_right and b_left <= a_right:
            # odd
            if total % 2:
                return min(a_right, b_right)
            # even
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            r = i - 1
        else:
            l = i + 1



print(findMedianSortedArrays([1,2], [3,4]))
