""" 
Description: 
Generates a fresh PasteBin paste with a list of a Pokemon's skills in it.
Usage:
  python pokemon_paste.py poke_name
Parameters:
  poke_name = Pokemon name
"""
import sys
import poke_api
import pastebin_api

def main():
    Poke_name = get_pokemon_name()
    poke_info = poke_api.get_pokemon_info(Poke_name)
    if poke_info is not None:
        paste_title, paste_body = get_paste_data(poke_info)
        paste_url = pastebin_api.post_new_paste(paste_title, paste_body, '1M')
        print(paste_url)

def get_pokemon_name():
    """Obtains the Pokemon name that was sent in as a command line argument.
    Script execution is aborted if no command line parameter is supplied.

    Returns:
        str: Pokemon name
    """
    # TODO: FN body
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        print(f"Error: Missing parameters.")
        return

def get_paste_data(pokemon_info):
    """Builds the title and body text for a PasteBin paste that lists a Pokemon's abilities.
    Args:
        pokemon_info (dict): Dictionary of Pokemon information
    Returns:
        (str, str): Title and body text for the PasteBin paste
    """    
    # TODO: Build the Title and paste body text
    pokemon_name = pokemon_info['name']
    title= f"{pokemon_name.capitalize()}'s Abilities"
    abilities_list = []

    for each_ability in pokemon_info['abilities']:
        abilities_list.append(each_ability['ability']['name'])
    body = '- ' + '\n- '.join(abilities_list)
    print(body)
    return (title,body)

if __name__ == '__main__':
    main()