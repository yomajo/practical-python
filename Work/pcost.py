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
        next(f)
        for line in f:
            try:
                row = line.split(',')
                shares = int(row[1])
                cost = float(row[2].strip())
                total_cost += shares * cost
            except ValueError:
                print(f'Error reading line: {line}')
    return total_cost

def calc_total_csv(fpath:str) -> float:
    '''calc cost of portfolio inside csv using csv standard library'''
    total_cost = 0
    with open(fpath, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for line in rows:
            try:
                shares = int(line[1])
                cost = float(line[2])
                total_cost += shares * cost
            except ValueError:
                print(f'Error reading line: {line}')
    return total_cost


def read_from_gzip():
    with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
        for line in f:
            print(line, end='')


def run():
    # total_cost = calc_total('Data/missing.csv')
    total_cost = calc_total_csv('Data/portfolio.csv')
    print(f'Total cost: {total_cost:,.2f}')
    # read_from_gzip()

if len(sys.argv) > 1:
    csv_file = sys.argv[1]
else:
    csv_file = 'Data/portfolio.csv'

total_cost = calc_total_csv(csv_file)
print(f'Total cost: {total_cost:,.2f}')
