# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(filename):
    '''opens a given portfolio file and reads it into a list of tuples'''
    portfolio = []
    types = [str, int, float]
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = dict(zip(headers, row))
            holding['shares'] = int(holding['shares'])
            holding['price'] = float(holding['price'])
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    '''returns price dict from passed csv file path'''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                name, price = row
                prices[name] = float(price)
    return prices


def portfolio_profit_loss():
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    cost = 0.0
    value = 0.0
    for holding in portfolio:
        name = holding['name']
        shares = holding['shares']
        price = holding['price']
        current_price = prices.get(name, price)
        # print(f'name: {name}, shares: {shares}, price: {price}')
        cost += shares * price
        value += shares * current_price
    print(f'Portfolio cost: {cost:,.2f}, current value: {value:,.2f}. P/L: {value-cost:,.2f}')

def make_report():
    report = []
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    for stock in portfolio:
        name, shares, price_paid = stock['name'], stock['shares'], stock['price']
        current_price = prices.get(name, price_paid)
        change = current_price - price_paid
        current_price_dollar = f'${current_price}'
        report_data = (name, shares, current_price_dollar, change)
        report.append(report_data)

    # printing report
    headers = ('Name', 'Shares', 'Price', 'Change')
    sep = '-'
    print(f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}'.format(headers))
    print(f'{sep:->10} '* 4)
    # body
    for name, shares, current_price, change in report:
        print(f'{name:>10} {shares:>10} {current_price:>10} {change:>10.2f}')


if __name__ == '__main__':
    pass
    # make_report()