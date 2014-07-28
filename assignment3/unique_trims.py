import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    # key: sequence ID
    # value: nucleotides
    value = record[1]
    trimmed_nucleotides = value[:-10]
    mr.emit_intermediate(len(trimmed_nucleotides), trimmed_nucleotides)

def reducer(key, list_of_values):
    def remove_duplicates(original_list):
        return list(set(original_list))
    # key: length of nucleotide strings
    # value: list of nucleotide strings
    for trimmed_nucleotide_string in remove_duplicates(list_of_values):
        mr.emit(trimmed_nucleotide_string)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)


