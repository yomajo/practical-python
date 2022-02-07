

class Stock():
    '''represents single stock object'''
    def __init__(self, name:str, shares:int, price:float):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
        '''returns stock purchase cost'''
        return self.shares * self.price

    def sell(self, sold_shares:int) -> int:
        '''reduces stock holding by sold_shares, returns remainder number of shares'''
        self.shares -= sold_shares
        return self.shares

    def __repr__(self) -> str:
        return f'Stock({self.name}, {self.shares}, {self.price})'
        
if __name__ == '__main__':
    pass