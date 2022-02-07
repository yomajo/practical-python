

class TableFormatter:
    def headings(self, headings):
        '''emit the table headings'''
        raise NotImplementedError()

    def row(self, row_data):
        '''emit a single row of table data'''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''Emit a table to plain-text format'''
    
    def headings(self, headers:list):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ') * len(headers))


    def row(self, row_data:list):
        for d in row_data:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''Output portfolio data in CSV format'''
    
    def headings(self, headers:list):
        print(','.join(headers))

    def row(self, row_data):
        print(','.join(row_data))

class HTMLTableFormatter(TableFormatter):
    '''Output portfolio data in HTML table format'''

    def headings(self, headers:list):
        htmled_data_str = ''.join([f'<th>{h}</th>' for h in headers])
        print(f'<tr>{htmled_data_str}</tr>')

    def row(self, row_data):
        htmled_data_str = ''.join([f'<td>{d}</td>' for d in row_data])
        print(f'<tr>{htmled_data_str}</tr>')
        
def create_formatter(fmt:str):
    '''returns formatter instance based on str abbreviation'''
    formatters = {
        'txt': TextTableFormatter,
        'csv': CSVTableFormatter,
        'html': HTMLTableFormatter,}
    try:
        formatter = formatters[fmt]()
        return formatter
    except KeyError as e:
        raise KeyError(f'Unknown formatter query: {e}')


if __name__ == '__main__':
    pass