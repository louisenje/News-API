from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_newssource,get_news_article,search_newsarticle,get_news,get_new_headlines
from ..models import Newsarticle,Newssource

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message='Hello World '
    general_news_sources=get_newssource('technology')
    technology_news_sources=get_newssource('technology')
    business_news_sources=get_newssource('business')
    sports_news_sources=get_newssource('sports')
    entertainment_news_sources=get_newssource('entertainment')
    health_news_sources=get_newssource('health')
    science_news_sources=get_newssource('science')
    # https://newsapi.org/v2/sources?apiKey=3a1f09f201904834870e3fdbb44430ee
    newsheadlines=get_new_headlines()
    title="Home-Welcome to NEWS sources Website"
    search_article=request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search',article_name=search_article))
    else:
        return render_template('index.html',title=title, general=general_news_sources,technology=technology_news_sources,business=business_news_sources,
        sports=sports_news_sources,entertainment=entertainment_news_sources,health=health_news_sources,science=science_news_sources,
        newsheadlines=newsheadlines)