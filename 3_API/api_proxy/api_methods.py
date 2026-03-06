import requests as r

BASE_URL = 'https://newsapi.org/v2'

def _make_request(endpoint: str, api_key: str, params: dict[str, str] = {}) -> dict[str, str]:
    """Func to make requests."""
    url = f"{BASE_URL}/{endpoint}"
    default_params = {'apiKey': api_key}

    if params:
        default_params.update(params)
    
    try:
        response = r.get(url, params=default_params, timeout=10)
        return response.json()
    except r.exceptions.RequestException as e:
        raise Exception(f"Ошибка в запросе к NewsAPI ({endpoint}): {e}")
    except ValueError as e:
        raise Exception(f"Ошибка типа JSON: {e}")


def get_top_headlines(api_key,
                      q: str,
                      country: str = '',
                      category: str = '',
                      sources: str = '',
                      page_size: int = 0) -> dict:

    # Paranms to Get the top headers. 
    allowed_params = {
        'q': q,
        'country': country,
        'category': category, 
        'sources': sources,
        'pageSize': page_size, 
    }
    
    # Remove all None's or 0's.
    params = {key: value for key, value in allowed_params.items() if value}

    return _make_request('top-headlines', api_key, params)


def get_everything(api_key: str = '',
                  q: str = '',
                  search_in: str = '',
                  sources: str = '',
                  domains: str = '',
                  exclude_domains: str = '',
                  from_date: str = '',
                  to_date: str = '',
                  language: str = '',
                  sort_by: str = '',
                  page_size: int = 0,
                  page: int = 0) -> dict:

    # Params to get all the articles and news. 
    allowed_params = {
        'q': q,
        'searchIn': search_in,
        'sources': sources,
        'domains': domains,
        'excludeDomains': exclude_domains,
        'from': from_date,
        'to': to_date,
        'language': language,
        'sortBy': sort_by,
        'pageSize': page_size,
        'page': page
    }

    # All params Except 0's or None's. 
    params = {key: value for key, value in allowed_params.items() if value}
    return _make_request('everything', api_key, params)
    

def get_sources(api_key: str = '',
                category: str = '',
                language: str = '',
                country: str = '') -> dict:

    # Params to Get the list of aviable params.
    allowed_params = {
        'category': category,
        'language': language,
        'country': country
    }
    
    # Each parameter except 0's.
    params = {key: value for key, value in allowed_params.items() if value is not None}

    return _make_request('top-headlines/sources', api_key, params)
