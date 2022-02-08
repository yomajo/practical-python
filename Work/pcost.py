# pcost.py
#
# Exercise 1.27
import gzip
import sys
from report import read_portfolio
from portfolio import Portfolio


def portfolio_cost(fpath:str) -> float:
    '''calc cost of portfolio inside csv'''
    total_cost = 0
    portfolio = read_portfolio(fpath)
    return portfolio.total_cost

def read_from_gzip():
    with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
        for line in f:
            print(line, end='')


def main():
    assert len(sys.argv) == 2, 'Unexpected number of args passed to main'
    portfolio_csv = sys.argv[1]
    cost = portfolio_cost(portfolio_csv)
    print(f'Portfolio cost: {cost:,.2f}')


if __name__ == '__main__':
    cost = portfolio_cost('Data/portfolio.csv')
    print(f'Portfolio cost: {cost:,.2f}')
    # main()