# pcost.py
#
# Exercise 1.27
import gzip
import csv
import sys

def calc_total(fpath:str) -> float:
    '''calc cost of portfolio inside csv'''
    total_cost = 0
    with open(fpath, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost += shares * price
            except ValueError:
                print(f'Row: {i} Couldn\'t convert: {row}')
    return total_cost


def read_from_gzip():
    with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
        for line in f:
            print(line, end='')


def run():
    total_cost = calc_total('Data/portfoliodate.csv')
    print(f'Total cost: {total_cost:,.2f}')
    # read_from_gzip()

# if len(sys.argv) > 1:
#     csv_file = sys.argv[1]
# else:
#     csv_file = 'Data/portfolio.csv'


if __name__ == '__main__':
    run()