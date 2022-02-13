import requests

def get_quotes():

    r = requests.get('http://quotes.stormconsultancy.co.uk/popular.json')

    r.json()

    return r.json()
      