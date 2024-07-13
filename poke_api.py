'''
A library to communicate with PokeAPI.
https://pokeapi.co/
'''
import requests
from sys import argv
import json

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = 'qZLQ10PeYijwkLLdyvTclwT5D85bOINu'

def main():
    if len(argv) < 2:
        print("Usage: python pokemon_paste.py <pokemon_name>")
        return

    pokemon_name = argv[1]
    
    # Get Pokémon information
    poke_information = get_pokemon_information(pokemon_name)
    
    if poke_information:
        # Post Pokémon information to PasteBin
        paste_url = post_to_pastebin(pokemon_name, poke_information)
        
        if paste_url:
            print(f"Getting information for {pokemon_name}...success")
            print(f"Posting new paste to PasteBin...success")
            print(f"Paste URL: {paste_url}")
        else:
            print(f"Getting information for {pokemon_name}...success")
            print(f"Posting new paste to PasteBin...failure")
    else:
        print(f"Getting information for {pokemon_name}...failure")

def get_pokemon_information(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    name = str(pokemon_name)
    name = name.strip().lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response_message = requests.get(url)

    if response_message.ok:
        response = response_message.json()
        return response
    else:
        print(f"Response code: {response_message.status_code} ({response_message.reason})")
        return None

def post_to_pastebin(pokemon_name, pokemon_info):
    """Posts the Pokemon information to PasteBin.

    Args:
        pokemon_name (str): Pokemon name
        pokemon_info (dict): Pokemon information as a dictionary

    Returns:
        str: URL of the newly created paste on PasteBin, if successful. Otherwise None.
    """
    print("Updating PasteBin with a fresh paste...", end='')
    paste_text = json.dumps(pokemon_info)
    
    post_params = {
        'api_dev_key': API_DEV_KEY,
        'api_option': 'paste',
        'api_paste_code': paste_text,
        'api_paste_name': f"{pokemon_name}_info",
        'api_paste_private': 0,  # Publicly listed
        'api_paste_expire_date': '1M'  # 1 month expiration
    }
    
    resp_message = requests.post(PASTEBIN_API_POST_URL, data=post_params)
    
    if resp_message.status_code == requests.codes.ok:
        print("Success!")
        return resp_message.text.strip()  # Assuming that the response contains just the paste URL
    else:
        print("Failure")
        print(f'Response code: {resp_message.status_code} ({resp_message.reason})')
        return None

if __name__ == '__main__':
    main()
