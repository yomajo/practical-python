import csv
from follow import follow
from report import read_portfolio
from tableformat import create_formatter

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [type_func(val) for type_func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def ticker(portfile:str='Data/portfolio.csv', logfile:str='Data/stocklog.csv', fmt:str='csv'):
    portfolio = read_portfolio(portfile)
    lines = follow(logfile)
    formatter = create_formatter(fmt)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)

    formatter.headings(['Name', 'Price', 'Change'])
    for stock in rows:
        row_data = [stock['name'], str(stock['price']), str(stock['change'])]
        formatter.row(row_data)    



if __name__ == '__main__':
    ticker()