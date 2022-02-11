from pprint import pprint

portfolio = [{'name': 'AA', 'price': 32.2, 'shares': 100},
            {'name': 'IBM', 'price': 91.1, 'shares': 60},
            {'name': 'CAT', 'price': 83.44, 'shares': 150},
            {'name': 'MSFT', 'price': 51.23, 'shares': 200},
            {'name': 'GE', 'price': 40.37, 'shares': 95},
            {'name': 'MSFT', 'price': 65.1, 'shares': 50},
            {'name': 'IBM', 'price': 70.44, 'shares': 110}]

def sort_my_list(portfolio:list) -> list:
    portfolio.sort(key=lambda s: s['name'], reverse=True)
    return portfolio

sorted_portfolio = sort_my_list(portfolio)

pprint(sorted_portfolio)