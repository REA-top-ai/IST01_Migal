from api_proxy.api_methods import *
from api_proxy.analytics import get_top_articles
import pprint as pp
import json

if __name__ == '__main__':
    API_KEY = '1053d4068827490c92d9f83a28fa8295'
    q='bitcoin'
    result = get_top_articles(q, API_KEY)
    pp.pprint(result)

    
