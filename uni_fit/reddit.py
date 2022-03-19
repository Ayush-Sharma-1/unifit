import json
import requests


def read_reddit_pw():
    """
    reads my reddit password from a file called 'pw.key'
    returns: a string which is either None, i.e no key found, or with a key
    'pw.key' is added to the .gitignore file
    """
    reddit_pw = None
    try:
        with open('pw.key', 'r') as f:
            reddit_pw = f.readline().strip()
    except:
        try:
            with open('../pw.key')as f:
                reddit_pw = f.readline().strip()
        except:
            raise IOError('pw.key file not found')
    
    if not reddit_pw:
        raise KeyError('Reddit Password not found')

    return reddit_pw


def read_reddit_key():
    """
    reads the REDDIT API key from a file called 'reddit.key'
    returns: a string which is either None, i.e no key found, or with a key
    'reddit.key' is added to the .gitignore file
    """
    reddit_api_key = None
    try:
        with open('reddit.key', 'r') as f:
            reddit_api_key = f.readline().strip()
    except:
        try:
            with open('../reddit.key')as f:
                reddit_api_key = f.readline().strip()
        except:
            raise IOError('reddit.key file not found')
    
    if not reddit_api_key:
        raise KeyError('Reddit key not found')

    return reddit_api_key


def get_posts():
    CLIENT_ID = 'ZUFA8UuWqrRnw83Mh4pHSw'
    SECRET_KEY = read_reddit_key()
    reddit_password = read_reddit_pw()

    
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {
        'grant_type': 'password',
        'username': 'zmeerza20',
        'password': reddit_password
        }
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization' : f'bearer {TOKEN}'}}
    params= {'limit':'50'}
    search_url = 'https://oauth.reddit.com/r/GlasgowUni/hot' 

    response = requests.get(search_url,headers=headers, params=params)
    reddit_results = response.json()

    #results = pd.DataFrame()
    results = []

    for result in reddit_results['data']['children']: # creates a dictionary that will contain all posts we would like to include
        results.append({
            'subreddit': result['data']['subreddit'],
            'title': result['data']['title'],
            'selftext': result['data']['selftext'],
            'upvote_ratio': result['data']['upvote_ratio'],
            'ups': result['data']['ups'],
            'downs': result['data']['downs'],
            'score': result['data']['score'],
            'url': result['data']['url']
        })
    return results


