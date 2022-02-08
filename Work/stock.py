

class Stock():
    '''represents single stock object'''

    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name:str, shares:int, price:float):
        self.name = name
        self.shares = shares
        self.price = price
    
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if isinstance(value, int):
            self._shares = value
        else:
            raise TypeError(f'Expected an integer for attribute: shares')

    @property
    def cost(self):
        '''returns stock purchase cost'''
        return self.shares * self.price

    def sell(self, sold_shares:int) -> int:
        '''reduces stock holding by sold_shares, returns remainder number of shares'''
        self.shares -= sold_shares
        return self.shares

    def __repr__(self) -> str:
        return f'Stock({self.name}, {self.shares}, {self.price})'
        
def run():
    msft = {'name': 'MSFT', 'shares': 150, 'price': 175.65}
    s = Stock(**msft)
    print(s.shares)
    s.new_attr = 'Wont allow me due to slots present...'

if __name__ == '__main__':
    # pass
    run()