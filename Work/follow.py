import os
import time
import csv

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line

def follow(filename:str):
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line

def run():
    lines = follow('Data/stocklog.csv')
    rows = csv.reader(lines)
    # ibm = filematch(lines, 'IBM')
    for rpw in rows:
        print(rpw)

if __name__ == '__main__':
    run()
    # portfolio = read_portfolio('Data/portfolio.csv')
    # for line in follow('Data/stocklog.csv'):
    #     fields = line.split(',')
    #     name = fields[0].strip('"')
    #     price = float(fields[1])
    #     change = float(fields[4])
    #     if name in portfolio:
    #         print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
