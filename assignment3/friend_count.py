import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)

def reducer(key, list_of_values):
    def count_unique(original_list):
        return len(set(original_list))
    # key: person
    # value: list of friends
    mr.emit((key, count_unique(list_of_values)))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)


