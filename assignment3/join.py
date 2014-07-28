import MapReduce
import sys


mr = MapReduce.MapReduce()


def mapper(record):
    table = record[0]
    order_id = record[1]
    mr.emit_intermediate(order_id, (table, record))

def reducer(key, list_of_values):
    # key: order_id
    # value: list of (table, record) pairs
    orders = []
    line_items = []
    for table, record in list_of_values:
        if table == "order":
            orders.append(record)
        else:  # if line_items
            line_items.append(record)

    for order in orders:
        for line_item in line_items:
            mr.emit(order + line_item)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)


