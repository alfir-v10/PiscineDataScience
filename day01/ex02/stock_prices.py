import sys


def get_stock_price(company_name):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    ticket = COMPANIES.get(company_name.capitalize())
    if ticket:
        return STOCKS.get(ticket)
    return "Unknown company"


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(get_stock_price(sys.argv[1]))
