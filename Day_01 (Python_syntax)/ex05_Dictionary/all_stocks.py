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
    tab = argv.split(',')
    for i in tab:
        if i.strip() == '':
            return
    for i in tab:
        company = i.strip().title()
        if company in companies:
            ticker = stocks[companies[company]]
            print(f"{company} stock price is {ticker}")
        elif company.upper() in stocks:
            for key, value in companies.items():
                if value == company.upper():
                    name_comp = key
            print(f"{company.upper()} is a ticker symbol for {name_comp}")
        else:
            print(f"{i.strip()} is an unknown company or an unknown ticker symbol")
        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        check_company(sys.argv[1])