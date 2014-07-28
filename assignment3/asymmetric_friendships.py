import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    friendship_edge = tuple(sorted(record))
    mr.emit_intermediate(friendship_edge, 1)

def reducer(key, list_of_values):
    # key: friendship_edge
    # value: list of occurrence counts
    if sum(list_of_values) != 1:
        return
    mr.emit(key)
    mr.emit(key[::-1])


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)



