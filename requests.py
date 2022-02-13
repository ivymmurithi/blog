import urllib.request,json
from models.randomposts_class import Random


base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['RANDOM_QUOTES_BASE_URL']

def get_quotes():
    get_quotes_url = base_url
    print(get_quotes_url)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
        quotes_results = None

        if get_quotes_response['quotes']:
            quotes_results_list = get_quotes_response['quotes']
            quotes_results = process_results(quotes_results_list)

        return quotes_results

def process_results(quotes_list):
    quotes_results = []

    for quotes_item in quotes_list:

        author = quotes_item.get('author')
        quote = quotes_item.get('quote')

        quote_object = Random(author,quote)
        quotes_results.append(quote_object)

    return quotes_results
      