import urllib.request,json#will help us create a connection to our API URL and send a request and json modules that will format the JSON response to a Python dictionary.
from .models import Newssource,Newsarticle



# Getting API Key and the urls
api_key = None
Newssource_url = None
Newsarticle_url = None
NewsarticleSearch_url = None
NEWSURL=None
NEWSHEADLINES=None
def config_request(app):

    global api_key,Newssource_url,Newsarticle_url,NewsarticleSearch_url,NEWSURL,NEWSHEADLINES

    api_key=app.config['NEWS_API_KEY']
    Newssource_url=app.config['NEWS_API_BASE_URL']
    Newsarticle_url=app.config['NEWS_ARTICLE_BASE_URL']
    NewsarticleSearch_url=app.config['NEWS_ARTICLE_SEARCH_BASE_URL']
    NEWSURL=app.config['NEWSURL']
    NEWSHEADLINES=app.config['NEWS_HEADLINES']


def get_newssource(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url=NEWSURL.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_newssource_data=url.read()
        get_newssource_response=json.loads(get_newssource_data)

        Newssource_results = None

        if get_newssource_response['sources']:
            Newssource_results_list=get_newssource_response['sources']
            Newssource_results=process_results(Newssource_results_list)

    return Newssource_results

def process_results(newssource_list):
    '''
    Function  that processes the Newssource_results and transform them to a list of Objects

    Args:
        Newssource_list: A list of dictionaries that contain news sources

    Returns :
       Newssource_results: A list of news objects
    '''
    Newssource_results = []
    for newssource_item in newssource_list:
        id=newssource_item.get('id')
        name=newssource_item.get('name')
        description=newssource_item.get('description')
        url=newssource_item.get('url')
        category=newssource_item.get('category')
        language=newssource_item.get('language')
        country=newssource_item.get('country')

        if name:
            Newssource_object=Newssource(id,name,description,url,category,language,country)
            Newssource_results.append(Newssource_object)
    return Newssource_results

def get_news_article(source):
    # source=news_article.get('url')
    get_Newsarticle_url=Newsarticle_url.format(source,api_key)

    with urllib.request.urlopen(get_Newsarticle_url)as url:
        Newsarticle_details_data=url.read()
        Newsarticle_details_response=json.loads(Newsarticle_details_data)

        newsarticle_object=None
        if Newsarticle_details_response['articles']:
            Newssource_results_list=Newsarticle_details_response['articles']
            newsarticle_object=process_results_article(Newssource_results_list)

            # print(Newsarticle_details_response)
          
    return newsarticle_object

def process_results_article(newsarticle_list):
    '''
    Function  that processes the Newssource_results and transform them to a list of Objects

    Args:
        Newssource_list: A list of dictionaries that contain news sources

    Returns :
       Newssource_results: A list of news objects
    '''
    Newsarticle_results = []

    for newsarticle_item in newsarticle_list:
        # print (Newsarticle_results)
        id=newsarticle_item.get('id')
        name=newsarticle_item.get('name')
        author=newsarticle_item.get('author')
        title=newsarticle_item.get('title')
        urlToImage=newsarticle_item.get('urlToImage')
        description=newsarticle_item.get('description')
        url=newsarticle_item.get('url')
        publishedAt=newsarticle_item.get('publishedAt')
        content=newsarticle_item.get('content')
        # print(newsarticle_item)
        if url:
            newsarticle_object=Newsarticle(id,name,author,title,urlToImage,description,url,publishedAt,content)
            Newsarticle_results.append(newsarticle_object)
    return Newsarticle_results

def search_newsarticle(articlesTitle):
    News_Article_search_URL=NewsarticleSearch_url.format(articlesTitle,api_key)
    with urllib.request.urlopen(News_Article_search_URL) as   url:
        search_Article_data=url.read()
        search_Article_response=json.loads(search_Article_data)

        search_Article_results=None

        if search_Article_response['articles']:
            search_Article_list=search_Article_response['articles']
            search_Article_results=process_results_article(search_Article_list)

    return search_Article_results
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newssource_url=NEWSURL.format(category,api_key)
    with urllib.request.urlopen(get_newssource_url) as url:
        get_newssource_data=url.read()
        get_newssource_response=json.loads(get_newssource_data)

        Newssource_results = None

        if get_newssource_response['sources']:
            Newssource_results_list=get_newssource_response['sources']
            Newssource_results=process_results(Newssource_results_list)

    return Newssource_results

def process_results(newssource_list):
    '''
    Function  that processes the Newssource_results and transform them to a list of Objects

    Args:
        Newssource_list: A list of dictionaries that contain news sources

    Returns :
       Newssource_results: A list of news objects
    '''
    Newssource_results = []
    for newssource_item in newssource_list:
        id=newssource_item.get('id')
        name=newssource_item.get('name')
        description=newssource_item.get('description')
        url=newssource_item.get('url')
        category=newssource_item.get('category')
        language=newssource_item.get('language')
        country=newssource_item.get('country')

        if name:
            Newssource_object=Newssource(id,name,description,url,category,language,country)
            Newssource_results.append(Newssource_object)
    return Newssource_results

