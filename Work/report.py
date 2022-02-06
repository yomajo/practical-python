# report.py
#
# Exercise 2.4
import sys
from fileparse import parse_csv
from stock import Stock


def read_portfolio(filename:str):
    '''opens a given portfolio file and reads it into a list of tuples'''
    with open(filename, mode='rt') as f:
        csv_contents = parse_csv(f=f, select=['name', 'shares', 'price'], types=[str, int, float])
        stocks = [Stock(s['name'], s['shares'], s['price']) for s in csv_contents]
    return stocks

def read_prices(filename:str):
    '''returns price dict from passed csv file path'''
    with open(filename, mode='rt') as f:
        contents = parse_csv(f=f, has_headers=False, types=[str, float], silence_errors=True)
    return contents

def portfolio_profit_loss():
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    cost = 0.0
    value = 0.0
    for s in portfolio:
        name = s.name
        shares = s.shares
        current_price = prices[name]
        cost += s.cost()
        value += shares * current_price
    print(f'Portfolio cost: {cost:,.2f}, current value: {value:,.2f}. P/L: {value-cost:,.2f}')

def get_report_obj(portfolio:list, prices:dict) -> list:
    '''returns report obj as list of tuple rows'''
    report = []
    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        current_price_dollar = f'${current_price}'
        report_data = (s.name, s.shares, current_price_dollar, change)
        report.append(report_data)
    return report

def portfolio_report(portfolio_csv_path:str='Data/portfolio.csv', prices_csv_path:str='Data/prices.csv'):
    '''collects and parses data from csv files and prints portfolio report to terminal'''
    portfolio = read_portfolio(portfolio_csv_path)
    prices = read_prices(prices_csv_path)
    report = get_report_obj(portfolio, prices)
    print_report(report)

def print_report(report:list):
    '''prints report to terminal'''
    headers = ('Name', 'Shares', 'Price', 'Change')
    sep = '-'
    print(f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}'.format(headers))
    print(f'{sep:->10} ' * len(headers))
    for name, shares, current_price, change in report:
        print(f'{name:>10} {shares:>10} {current_price:>10} {change:>10.2f}')

def main():
    assert len(sys.argv) == 3, 'Error parsing command line arguments'
    portfolio_csv_path = sys.argv[1]
    prices_csv_path = sys.argv[2]
    portfolio_report(portfolio_csv_path, prices_csv_path)


if __name__ == '__main__':
    # main()
    portfolio_report()