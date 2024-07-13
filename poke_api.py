'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests
from sys import argv
import json

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Testing the get_pokemon_info() function
    # Make sure breakpoints are used to view returned dictionary
    poke_information = get_pokemon_information("Rockruff")
    return

def get_pokemon_information(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    name = str(pokemon_name)
    name = name.strip().lower()

    # TODO: Build a clean URL and use it to send a GET request
    url = f"https://pokeapi.co/api/v2/pokemon/" + name
    response_message = requests.get(url)

    print(f'Getting information for {pokemon_name}...', end="")

    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if response_message.ok:
        print('success')
        response = response_message.json()
        return response
    else:
        print("failure")
        print(f"Response code: {response_message.status_code} ({response_message.reason})")

    # TODO: If the GET request failed, print the error reason and return None

    return

if __name__ == '__main__':
    main()