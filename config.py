import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?apiKey={}'
    NEWSURL='https://newsapi.org/v2/sources?category{}&apiKey={}'
    NEWS_ARTICLE_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_ARTICLE_SEARCH_BASE_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_HEADLINES='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'

    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')

