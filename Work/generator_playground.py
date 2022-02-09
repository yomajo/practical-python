
def filematch(filename:str, substr:str):
    '''generator emiting text file lines, that contain substr'''
    with open(filename, mode='r') as f:
        for line in f:
            if substr in line:
                yield line



def run():
    search_for = 'IBM'
    for line in filematch('Data/portfolio.csv', search_for):
        print(line, end='')

if __name__ == '__main__':
    run()