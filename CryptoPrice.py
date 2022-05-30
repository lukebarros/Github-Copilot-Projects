'''Get price from cryptocompare and save it to a file'''

def get_price(url):
    '''Get price from cryptocompare and save it to a file'''
    import requests
    import json
    import os

    # Get price from cryptocompare
    response = requests.get(url)
    response.raise_for_status()
    price_data = response.json()

    # Save price to a file
    if not os.path.exists('price_data.json'):
        with open('price_data.json', 'w') as file:
            json.dump(price_data, file)
    else:
        print('File already exists')

def main():
    '''Get price from cryptocompare and save it to a file'''
    url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'
    get_price(url)

def test_get_price():
    '''Test get_price'''
    url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'
    assert get_price(url) == None

def test_main():
    '''Test main'''
    url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'
    assert main() == None

def test_get_price_fail():
    '''Test get_price'''
    url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'
    assert get_price(url) == None

