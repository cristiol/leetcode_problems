"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


def searchMatrix(matrix, target):

    new_list = [item for sublist in matrix for item in sublist]

    l = 0
    r = len(new_list) - 1

    while l < r:
        mid = (l + r)// 2
        if target == new_list[mid]:
            return True
        elif target < new_list[mid]:
            r = mid - 1
        else:
            l = mid + 1

    if new_list[l] == target:
        return True
    else:
        return False



print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=60))