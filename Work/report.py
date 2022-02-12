# report.py
#
# Exercise 2.4
import sys
from fileparse import parse_csv
from tableformat import create_formatter
from portfolio import Portfolio
import logging

logging.basicConfig(
    filename = 'app.log',            # Name of the log file (omit to use stderr)
    filemode = 'w',                  # File mode (use 'a' to append)
    level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
)


def read_portfolio(filename:str, **opts):
    '''opens a given portfolio file and reads it into a list of tuples'''
    with open(filename, mode='rt') as f:
        portfolio = Portfolio.from_csv(f, **opts)        
    return portfolio

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
        current_price_dollar = f'${current_price:0.2f}'
        report_data = (s.name, s.shares, current_price_dollar, change)
        report.append(report_data)
    return report

def portfolio_report(portfolio_csv_path:str='Data/portfolio.csv', prices_csv_path:str='Data/prices.csv', fmt:str='txt'):
    '''collects and parses data from csv files and prints portfolio report using preferred formatter (fmt arg)'''
    portfolio = read_portfolio(portfolio_csv_path)
    prices = read_prices(prices_csv_path)
    report = get_report_obj(portfolio, prices)

    formatter = create_formatter(fmt)
    print_report(report, formatter)
    logging.info('Finished without errors')

def print_report(report:list, formatter):
    '''prints report to terminal'''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, current_price, change in report:
        row_data = [ name, str(shares), current_price, f'{change:0.2f}']
        formatter.row(row_data)

def main():
    assert len(sys.argv) >= 3, 'Error parsing command line arguments'
    portfolio_csv_path = sys.argv[1]
    prices_csv_path = sys.argv[2]
    fmt = sys.argv[3] if sys.argv[3] else 'txt'
    portfolio_report(portfolio_csv_path, prices_csv_path, fmt)


if __name__ == '__main__':
    # main()
    portfolio_report(fmt='txt')