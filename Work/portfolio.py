from collections import Counter
from fileparse import parse_csv
from stock import Stock

class Portfolio:

    def __init__(self):
        self.holdings = []

    def __iter__(self):
        return self.holdings.__iter__()

    def __len__(self):
        return len(self.holdings)
    
    def __getitem__(self, index):
        return self.holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self.holdings])

    def append(self, holding):
        if not isinstance(holding, Stock):
            raise TypeError(f'attempted to add non {Stock.__class__} instance to Portfolio')
        self.holdings.append(holding)

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float], **opts)
        for d in portdicts:
            self.append(Stock(**d))
        return self

    @property
    def total_cost(self):
        return sum([s.cost for s in self.holdings])

    def tabulate_shares(self):
        total_shares = Counter()
        for s in self.holdings:
            total_shares[s.name] += s.shares
        return total_shares




def run():
    pass

if __name__ == '__main__':
    pass
    # run()