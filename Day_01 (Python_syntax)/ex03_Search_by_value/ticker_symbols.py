import sys

def check_ticker(argv):
    companies = {
    'Apple' : 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix' : 'NFLX',
    'Tesla' : 'TSLA',
    'Nokia' : 'NOK'
    }

    stocks = {
        'AAPL' : 287.73,
        'MSFT' : 173.79,
        'NFLX' : 416.90,
        'TSLA' : 724.88,
        'NOK' : 3.37
    }
    ticker = argv.upper()
    ticker_present = stocks.get(argv.upper())
    if ticker_present is None:
        print('Unknown company')
    else:
        for company, short in companies.items():
            if ticker == short:
                print(company, stocks[ticker])
        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        check_ticker(sys.argv[1])