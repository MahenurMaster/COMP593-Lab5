'''
An interface library for the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = 'qZLQ10PeYijwkLLdyvTclwT5D85bOINu'

def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    #TO DO: function written s group

    print(f'updating PasteBin with a fresh paste...', end="")
    post_params = {'api_dev_key' : API_DEV_KEY,
                   'api_option': 'paste',
                   'api_paste_code' : body_text,
                   'api_paste_name' : title,
                   'api_paste_private' : 0 if listed else 1,
                   'api_paste_expire_date' : expiration
                   }

    response_message = requests.post(PASTEBIN_API_POST_URL, data = post_params)
    
    #paste check

    if response_message.status_code == requests.codes.ok:
        print('Success')
    else: 
        print('Failure')
        print(f'Response code: {response_message.status.code} ({response_message.reason})')

    return response_message.text
