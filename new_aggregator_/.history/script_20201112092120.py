import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import re
import time
import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://bruhuser:griffith@cluster0.ccamn.mongodb.net/articles?retryWrites=true&w=majority")
db = client.get_database('articles')
class Source:
    def __init__(self, source_url):
        # change source_url dependent on actual source
        self.source_url = source_url
        self.articles = []
        if source_url == "http://www.nytimes.com":
            self.get_article_urls_from_source('css-6p6lnl', None, None)
        elif source_url == "https://www.npr.org/":
            self.get_article_urls_from_source('story-text', None, None)
        elif source_url == "https://www.reuters.com/":
            self.get_article_urls_from_source('story-content', None, None)
        elif source_url == "https://www.wired.com/":
            self.get_article_urls_from_source('card_component', None, None)
        elif source_url == "http://techcrunch.com":
            self.get_article_urls_from_source('post-block', 'class', 'post-block__title__link')
        elif source_url == "https://www.economist.com/":
            self.get_article_urls_from_source('teaser', 'class', 'headline-link')
        elif source_url == "https://www.bbc.com/news":
            self.get_article_urls_from_source('gs-c-promo-body', None, None)
        elif source_url == 'https://www.theverge.com/':
            self.get_article_urls_from_source('c-entry-box--compact__body', None, None)

    def get_article_urls_from_source(self, find_tag1, link1, link2):
        # do something with beautiful soup to return list of urls for article
        response = requests.get(self.source_url)
        doc = BeautifulSoup(response.text, 'html.parser')
        story = doc.find_all('div', {'class': find_tag1})
        for story in story[:15]:
            article = story.find('a', {link1: link2})
            if self.source_url in ("https://www.npr.org/", "http://techcrunch.com", "https://www.theverge.com/"):
                article = article['href']
            else:
                article = self.source_url + article['href']
            if article is not None:
                self.articles.append(article)


class Article:
    def __init__(self, url, source_url):
        self.url = url
        self.source_url = source_url
        self.headline = ""
        self.summary = ""
        if self.source_url == "http://www.nytimes.com":
            self.parse_article('div', 'class', 'css-1vkm6nb', 'p', None, None)
        elif self.source_url == "https://www.npr.org/":
            print('whoops')


    def parse_article(self, head1, head2, head3, sum1, sum2, sum3):
        # use beautiful soup to parse actual article
        response = requests.get(self.url)
        doc = BeautifulSoup(response.text, 'html.parser')
        self.headline = doc.find(head1, {head2:head3}).text
        self.summary = doc.find(sum1, {sum2:sum3}).text
