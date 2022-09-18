import sys


def get_stock_price(company_name, companies, stocks):
    ticket = companies.get(company_name.capitalize())
    if ticket:
        return stocks.get(ticket)
    return "Unknown company"


def get_name_and_price(company_name_or_ticket):
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
    name_and_price = []
    company_name = company_name_or_ticket.capitalize()
    if company_name in COMPANIES:
        name_and_price.append(company_name)
        price = get_stock_price(company_name, COMPANIES, STOCKS)
        if isinstance(price, float):
            name_and_price.append(str(price))
            return f"{name_and_price[0]} stock price is {name_and_price[1]}"

    ticket = company_name_or_ticket.upper()
    COMPANIES_REV = {v: k for k, v in COMPANIES.items()}
    if ticket in COMPANIES_REV:
        return f"{ticket} is a ticker symbol for {COMPANIES_REV[ticket]}"
    return f"{company_name_or_ticket} is an unknown company or an unknown ticker symbol"


if __name__ == '__main__':
    if len(sys.argv) == 2:
        argv = sys.argv[1].split(',')
        if "" not in [a.replace(' ', '') for a in argv]:
            for arg in argv:
                print(get_name_and_price(arg.strip()))
