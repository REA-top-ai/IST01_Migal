from api_proxy.api_methods import *
import pprint as pp

if __name__ == '__main__':
    # result = get_top_headlines(q='apple', api_key='1053d4068827490c92d9f83a28fa8295')
    result = get_everything(q="bitcoin", api_key="eb06bb24ef204dee8e6463bd4e5d6a78")
    pp.pprint(result)
