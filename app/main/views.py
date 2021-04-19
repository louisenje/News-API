from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_newssource,get_news_article,search_newsarticle,get_news,get_new_headlines
from ..models import Newsarticle,Newssource