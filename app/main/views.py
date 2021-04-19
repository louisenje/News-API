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
    # https://newsapi.org/v2/sources?apiKey=1a7a89e9390e47fcb1f7fb977320f71a
    newsheadlines=get_new_headlines()
    title="Home-Welcome to NEWS sources Website"
    search_article=request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search',article_name=search_article))
    else:
        return render_template('index.html',title=title, general=general_news_sources,technology=technology_news_sources,business=business_news_sources,
        sports=sports_news_sources,entertainment=entertainment_news_sources,health=health_news_sources,science=science_news_sources,
        newsheadlines=newsheadlines)

@main.route('/news/<source>')
def news(source):
    '''
    View news article function that returns the news articles page and its data
    '''
    newsarticle=get_news_article(source)
    # title=f'{newsarticle.title}'
    print(newsarticle)
    return render_template ('news.html',news=newsarticle)
@main.route('/search/<article_name>')
def search(article_name): 
    """
    View FUnction to display the search results
    """
    search_newsarticle_list=article_name.split(" ")
    search_newsarticle_format="+".join(search_newsarticle_list)
    searched_newsarticles=search_newsarticle(search_newsarticle_format)
    title=f'search results for {article_name}'
    return render_template('search.html',articles=searched_newsarticles)

@main.route('/categories/<category>')
def categories(category):
    '''
    View root page function that returns the category page and its data
    '''
    general_news_sources=get_news('general')
    technology_news_sources=get_news('technology')
    business_news_sources=get_news('business')
    sports_news_sources=get_news('sports')
    entertainment_news_sources=get_news('entertainment')
    health_news_sources=get_news('health')
    science_news_sources=get_news('science')
    # https://newsapi.org/v2/sources?apiKey=1a7a89e9390e47fcb1f7fb977320f71a
    title="General News"
    category=request.args.get('general')
    if category:
        return redirect(url_for('.category',general=general_news_sources))
    else:
        return render_template('category.html',title=title,general=general_news_sources)

 