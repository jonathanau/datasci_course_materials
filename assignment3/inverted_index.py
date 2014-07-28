import MapReduce
import sys


mr = MapReduce.MapReduce()


def remove_duplicates(original_list):
    return list(set(original_list))

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of document identifiers
    mr.emit((key, remove_duplicates(list_of_values)))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

