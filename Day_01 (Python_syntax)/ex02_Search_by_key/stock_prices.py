import sys

def check_company(argv):
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
    company_name = companies.get(argv.title())
    if company_name is None:
        print('Unknown company')
    else:
        print(stocks[company_name])
        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        check_company(sys.argv[1])