#!/usr/bin/python3
"""
rotating a 2d matrix
"""


def reverseRows(matrix, n):
    """
    reverses the rows of a matrix
    """
    for i in range(n):
        j = 0
        k = n-1
        while j < k:
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][k]
            matrix[i][k] = temp
            j += 1
            k -= 1


def transpose(matrix, n):
    """
    transposes a matrix
    """
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


def rotate_2d_matrix(matrix):
    n = len(matrix)
    transpose(matrix, n)
    reverseRows(matrix, n)
