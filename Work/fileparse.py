# fileparse.py
#
# Exercise 3.3

import csv
from pprint import pprint


def parse_csv(filename:str, select:list=None, types:list=None, has_headers:bool=True, delimiter=',', silence_errors:bool=False):
    '''Parse a csv file into a list of records
    
    Returns dict for files without headers and list of dicts - with headers'''
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
        for i, row in enumerate(rows, start=1):
            if not row:
                continue
            
            if has_headers:
                if indices:
                    # reduce row list to only those matching select headers
                    row = [row[i] for i in indices]
                
                if types:
                    # transform data value types
                    try:
                        row = [func(val) for func, val in zip(types, row)]
                    except ValueError as e:
                        if not silence_errors:
                            print(f'Error parsing row: {i}. Error: {e}')
                        continue
                    record = dict(zip(headers, row))
            else:
                # return records as tuples
                if types:
                    try:
                        record = tuple([func(val) for func, val in zip(types, row)])
                    except ValueError as e:
                        if not silence_errors:
                            print(f'Error parsing row: {i}. Error: {e}')
                        continue
                else:
                    record = tuple([val for val in row])
            records.append(record)
    return records if has_headers else dict(records)

if __name__ == '__main__':
    data = parse_csv('Data/missing.csv', types=[str, int, float], silence_errors=False)
    pprint(data)
    print(type(data))