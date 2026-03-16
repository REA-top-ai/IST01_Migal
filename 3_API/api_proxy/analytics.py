from .api_methods import get_everything 

def get_top_articles(q, api_key): 
    """Function to get Top-50 articles satisfying to a specific conditions."""
    page_size = 50 
    required_count = 50 
    result = []
    n_page = 1

    while len(result) < required_count:
        """Loop to take every 50 art. and see if there s enough for output."""
        articles_for_page = get_everything(q=q, api_key=api_key, page_size=page_size, page=n_page)
        
        for article in articles_for_page['articles']:
            description = article.get('description', '')
            if article.get('title') and article.get('url') and description is not None and len(description)>= 50: # Conditions 
                result.append({'title': article.get('title'),
                               'source name': article.get('source').get('name'),
                               'published': article.get('publishedAt'),
                               'author': article.get('author')})
        
        # If there is 50 or more articles, print them.
        if len(result) >= required_count:
            return result[:50]
        
        # Else move to the next page.
        n_page += 1
