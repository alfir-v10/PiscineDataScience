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
    company_name_or_ticket = company_name_or_ticket.capitalize()
    if company_name_or_ticket in COMPANIES:
        name_and_price.append(company_name_or_ticket)
        price = get_stock_price(company_name_or_ticket, COMPANIES, STOCKS)
        if isinstance(price, float):
            name_and_price.append(str(price))
            return " ".join(name_and_price)
        return "Unknown company"

    company_name_or_ticket = company_name_or_ticket.upper()
    COMPANIES_REV = {v: k for k, v in COMPANIES.items()}
    if company_name_or_ticket in STOCKS and company_name_or_ticket in COMPANIES_REV:
        name_and_price.append(COMPANIES_REV[company_name_or_ticket])
        name_and_price.append(str(STOCKS[company_name_or_ticket]))
        return " ".join(name_and_price)
    return "Unknown company"


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(get_name_and_price(sys.argv[1]))
