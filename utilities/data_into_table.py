# should be installed 'prettytable' module for data looks like a table, not as a list
from prettytable import PrettyTable


def make_data_as_a_table(data, *args):
    table = PrettyTable(*args)
    print('\n')
    for row in data:
        table.add_row(row)

    return table