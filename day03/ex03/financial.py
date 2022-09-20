import sys
import requests
from bs4 import BeautifulSoup
import time


def financial(ticker_symbol, field_of_table):
    time.sleep(5)
    ticker_symbol = ticker_symbol.lower()
    url = f'https://finance.yahoo.com/quote/{ticker_symbol}/financials?p={ticker_symbol}'
    res = requests.get(url, headers={'User-Agent': 'Custom'})
    if res.status_code != 200:
        raise ValueError("URL doesn't exist")
    
    soup = BeautifulSoup(res.text, "html.parser")
    value = soup.find_all('div', class_ ='fi-row')
    result = []
    for val in value:
        if val.span.text == field_of_table:
            result.append(val.span.text)
            value = val.find_all('div', class_='Ta(c)')
            for val in value:
                result.append(val.text)
    if not result:
        raise ValueError(f"Field {field_of_table} in {ticker_symbol} doesn't exist")
    return result


if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            print(financial(sys.argv[1], sys.argv[2]))
        except Exception as e:
            print(e)
    else:
        raise ValueError("Invalid arguments")

