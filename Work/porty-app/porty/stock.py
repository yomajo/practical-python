from .typedproperty import String, Integer, Float

class Stock():
    '''represents single stock object'''

    __slots__ = ('_name', '_shares', '_price')
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name:str, shares:int, price:float):
        self.name = name
        self.shares = shares
        self.price = price
    
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
    # s.new_attr = 'Wont allow me due to slots present...'
    # s.price = '743.65'

if __name__ == '__main__':
    # pass
    run()