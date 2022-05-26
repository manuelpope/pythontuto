import sys


def csv_reader(file_name, headers: bool = False):
    '''
    headers true -> skip those
    '''
    file = open(file_name)
    result = file.read().split("\n")
    if(not headers):

        return result

    return result[1:]


def csv_reader_yield(file_name, headers: bool = False):
    '''
    headers true -> skip those
    '''
    g = (row for row in open(file_name, "r"))

    if(headers):
        next(g)
        try:
            while True:
                yield(next(g))
        except StopIteration:
            pass

    for row in g:

        yield row


if __name__ == "__main__":
    csv_gen = csv_reader(
        "electronic-card-transactions-april-2022-csv-tables.csv",
         headers=True)
    row_count = 0

    for row in csv_gen:
        row_count += 1
        if(row_count == 18636):
            print(row)

    print(f"Row count is {row_count}")
    print(f"size : {sys.getsizeof(csv_gen)} bytes")

    csv_gen = csv_reader_yield(
        "electronic-card-transactions-april-2022-csv-tables.csv", headers=True)
    row_count = 0

    for row in csv_gen:
        row_count += 1
        if(row_count == 18636):
            print(row)

    print(f"Row count is {row_count}")
    print(f"size gen : {sys.getsizeof(csv_gen)} bytes")

    # of course youy could do following declaration gen comprenhension instead of a function:
    '''
    csv_gen = (row for row in open(file_name))
    Output :
    Row count is 18638
    size : 150048 bytes
    Row count is 18637
    size gen : 112 bytes
    '''
