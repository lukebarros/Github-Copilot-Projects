'''Get pokemon data from the web and save it to a file'''

def get_pokemon_data(url):
    '''Get pokemon data from the web and save it to a file'''
    import requests
    import json
    import os

    # Get pokemon data from the web
    response = requests.get(url)
    response.raise_for_status()
    pokemon_data = response.json()

    # Save pokemon data to a file
    if not os.path.exists('pokemon_data.json'):
        with open('pokemon_data.json', 'w') as file:
            json.dump(pokemon_data, file)
    else:
        print('File already exists')

def main():
    '''Get pokemon data from the web and save it to a file'''
    url = 'https://pokeapi.co/api/v2/pokemon/'
    get_pokemon_data(url)

def test_get_pokemon_data():
    '''Test get_pokemon_data'''
    url = 'https://pokeapi.co/api/v2/pokemon/'
    assert get_pokemon_data(url) == None

def test_main():
    '''Test main'''
    url = 'https://pokeapi.co/api/v2/pokemon/'
    assert main() == None

def test_get_pokemon_data_fail():
    '''Test get_pokemon_data'''
    url = 'https://pokeapi.co/api/v2/pokemon/'
    assert get_pokemon_data(url) == None

def test_main_fail():
    '''Test main'''
    url = 'https://pokeapi.co/api/v2/pokemon/'
    assert main() == None

def test_get_pokemon_data_fail():
    '''Test get_pokemon_data'''
    url = 'https://pokeapi.co/api/v2/pokemon/'
    assert get_pokemon_data(url) == None

