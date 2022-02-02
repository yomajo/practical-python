# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv

def read_portfolio(filename):
    '''opens a given portfolio file and reads it into a list of tuples'''
    return parse_csv(filename=filename, select=['name', 'shares', 'price'], types=[str, int, float])

def read_prices(filename):
    '''returns price dict from passed csv file path'''
    return parse_csv(filename=filename, has_headers=False, types=[str, float], silence_errors=True)

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
        cost += shares * price
        value += shares * current_price
    print(f'Portfolio cost: {cost:,.2f}, current value: {value:,.2f}. P/L: {value-cost:,.2f}')

def get_report_obj(portfolio:list, prices:dict) -> list:
    '''returns report obj as list of tuple rows'''
    report = []
    for stock in portfolio:
        name, shares, price_paid = stock['name'], stock['shares'], stock['price']
        current_price = prices.get(name, price_paid)
        change = current_price - price_paid
        current_price_dollar = f'${current_price}'
        report_data = (name, shares, current_price_dollar, change)
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


if __name__ == '__main__':    
    files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
    for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, 'Data/prices.csv')
        print()