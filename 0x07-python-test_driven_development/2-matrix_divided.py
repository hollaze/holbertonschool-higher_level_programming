#!/usr/bin/python3
''' matrix divided function'''

matrix_typeError = "matrix must be a matrix (list of lists) of integers/floats"
div_typeError = "div must be a number"
div_zeroError = "division by zero"
row_typeError = "Each row of the matrix must have the same size"


def matrix_divided(matrix, div):
    '''
    divides all elements of a matrix by div

        Parameters:
                matrix  (lists of lists)
                div     (int / float)

        Returns:
                a new matrix with all elements divided
    '''

    new_matrix = []

    if type(matrix) is not list and len(matrix) == 0:
        raise TypeError(matrix_typeError)
    if type(div) not in (int, float):
        raise TypeError(div_typeError)
    if div == 0:
        raise ZeroDivisionError(div_zeroError)

    for row in matrix:
        new_row = []

        if type(row) is not list and len(row) == 0:
            raise TypeError(matrix_typeError)
        if len(row) != len(matrix[0]):
            raise TypeError(row_typeError)

        for number in row:
            if type(div) not in (int, float):
                raise TypeError(div_typeError)
            new_row.append(round((number / div), 2))

        new_matrix.append(new_row)

    return new_matrix
