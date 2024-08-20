"""
1252. Cells with Odd Values in a Matrix
There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

For each location indices[i], do both of the following:

Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.
"""


def oddCells(m, n, indices):

    rows, columns = [0]*m, [0]*n

    for r, c in indices:
        rows[r] += 1
        columns[c] += 1

    odd_sum = 0

    for r in rows:
        for c in columns:
            if (r+c) % 2:
                odd_sum += 1

    return odd_sum

#print(oddCells(2,3,[[0,1],[1,1]]))