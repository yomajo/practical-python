# fileparse.py
#
# Exercise 3.3

import csv
from pprint import pprint


def parse_csv(filename:str, select:list=None, types:list=None, has_headers:bool=True, delimiter=','):
    '''Parse a csv file into a list of records'''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        
        if has_headers:
            headers = next(rows)

            if select:
                indices = [headers.index(header) for header in select]
                headers = select
            else:
                indices = []

        records = []
        for row in rows:
            if not row:
                continue
            
            if has_headers:
                if indices:
                    # reduce row list to only those matching select headers
                    row = [row[i] for i in indices]
                
                if types:
                    # transform data value types
                    row = [func(val) for func, val in zip(types, row)]
                
                record = dict(zip(headers, row))
            else:
                # return records as tuples
                if types:
                    record = tuple([func(val) for func, val in zip(types, row)])
                else:
                    record = tuple([val for val in row])
            records.append(record)
    return records

if __name__ == '__main__':
    # data = parse_csv('Data/portfolio.csv', select=None, types=[str, int, float])
    data = parse_csv('Data/portfolio.dat', delimiter=' ', types=[str, int, float])
    pprint(data)
    print(type(data))
