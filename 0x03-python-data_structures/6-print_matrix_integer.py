#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for x in matrix:
            for ele in x:
                print("{:d}".format(ele), end=" "
                      if ele != x[-1] else '\n')
    else:
        print()
