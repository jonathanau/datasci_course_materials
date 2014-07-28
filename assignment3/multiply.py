from collections import defaultdict
import MapReduce
import sys


mr = MapReduce.MapReduce()
L = M = N = 5  # matrix dimensions


def mapper(record):
    matrix = record[0]
    if matrix == "a":
        _, i, j, value = record
        for k in range(N):
            mr.emit_intermediate((i, k), (matrix, i, j, value))
    else:  # if "b"
        _, j, k, value = record
        for i in range(L):
            mr.emit_intermediate((i, k), (matrix, j, k, value))

def reducer(key, list_of_values):
    # key: element position in result matrix
    # value: (matrix, row, column, value)
    matrix_values = {
            "a": defaultdict(int),
            "b": defaultdict(int),
            }
    for matrix, row, column, value in list_of_values:
        matrix_values[matrix][(row, column)] = value

    i, k = key
    result_value = 0
    for i, j in matrix_values["a"]:
        result_value += matrix_values["a"][(i, j)] * matrix_values["b"][(j, k)]
    mr.emit((i, k, result_value))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)


