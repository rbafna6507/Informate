import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import re
import time
import pymongo
import dns

client = pymongo.MongoClient("mongodb+srv://bruhuser:griffith@cluster0.ccamn.mongodb.net/articles?retryWrites=true&w=majority")
db = client.get_database('articles')
collections = [db.nytimes, db.reuters, db.wired, db.economist, db.bbc]

class Queue():
    def __init__(self, list):
        self.list = list
    def enqueue(self, new_element):
        self.list.append(new_element)
    def dequeue(self):
        return self.list.pop(0)
    def peek(self):
        return self.list[0]

class Source:
    def __init__(self, source_url):
        # change source_url dependent on actual source
        self.source_url = source_url
        self.articles = []
        if source_url == "http://www.nytimes.com/":
            self.get_article_urls_from_source('css-6p6lnl', None, None)
        elif source_url == "https://www.reuters.com/":
            self.get_article_urls_from_source('story-content', None, None)
        elif source_url == "https://www.wired.com":
            self.get_article_urls_from_source('card-component', None, None)
        elif source_url == "https://www.economist.com/":
            self.get_article_urls_from_source('teaser', 'class', 'headline-link')
        elif source_url == "https://www.bbc.com":
            self.get_article_urls_from_source('media__content', 'class', 'media__link')

    def get_article_urls_from_source(self, find_tag1, link1, link2):
        # do something with beautiful soup to return list of urls for article
        response = requests.get(self.source_url)
        doc = BeautifulSoup(response.text, 'html.parser')
        story = doc.find_all('div', {'class': find_tag1})
        for story in story[:15]:
            article = story.find('a', {link1: link2})
            if self.source_url in ("https://www.wsj.com/news/latest-headlines?mod=wsjheader", "http://techcrunch.com", "https://www.theverge.com/") and article != None:
                article = article['href']
            elif self.source_url == "https://www.bbc.com/news":
                article = "https://bbc.com" + article['href']
            elif article != None:
                article = self.source_url + article['href']
                regex = re.compile(self.source_url + self.source_url)
                article = regex.sub(self.source_url, article).strip()
            if article is not None:
                self.articles.append(article)


class Article:
    def __init__(self, url, source_url):
        self.url = url
        self.source_url = source_url
        self.headline = None
        self.summary = None

        if self.source_url == "http://www.nytimes.com/":
            self.parse_article('h1', None, None, 'p', "class", 'evys1bk0')

        elif source_url == "https://www.reuters.com/":
            self.parse_article('h1', 'class', 'Headline-headline-2FXIq Headline-black-OogpV ArticleHeader-headline-NlAqj', 'p', 'class', 'Paragraph-paragraph-2Bgue ArticleBody-para-TD_9x')

        elif source_url == "https://www.wired.com":
            self.parse_article('h1', None, None, 'div', 'class', 'content-header__dek')

        elif source_url == "https://www.economist.com/":
            self.parse_article('h1', None, None, 'p', 'class', 'article__description')

        elif source_url == "https://www.bbc.com":
            try:
                self.parse_article('h1', 'class', 'css-1c1994u-StyledHeading e1fj1fc10', 'p', None, None)
                if self.headline == None or self.summary == None:
                    self.parse_article('div', 'class', 'article-headline__text b-reith-sans-font b-font-weight-300', 'div', 'class', 'article__intro')
                    if self.headline == None or self.summary == None:
                        self.parse_article('h1', None, None, 'b', 'class', 'css-14iz86j-BoldText e5tfeyi0')
            except:
                    self.headline = None
                    self.summary= None



    def parse_article(self, head1, head2, head3, sum1, sum2, sum3):
        # use beautiful soup to parse actual article
        response = requests.get(self.url)
        doc = BeautifulSoup(response.text, 'html.parser')
        tempHead = doc.find(head1, {head2:head3})
        if tempHead != None:
            self.headline = tempHead.text
            tempSumm = doc.find(sum1, {sum2:sum3})
            if tempSumm != None:
                self.summary = tempSumm.text
            else:
                self.headline = None
                self.summary = None

def upload_to_mongo(list_of_articles, collection):
    for article in list_of_articles:
        if article.headline == None or article.summary == None:
            list_of_articles.remove(article)
    list_of_articles = Queue(list_of_articles)
    for inputted_article in collection.find():
        articlez = list_of_articles.dequeue()
        collection.update_one(inputted_article, {'$set': {'Headline': articlez.headline, 'Info':articlez.summary,'Link':articlez.url}})

def parse_sources():
    sources = ['http://www.nytimes.com/', 'https://www.reuters.com/', 'https://www.wired.com', 'https://www.economist.com/', 'https://www.bbc.com']

    for source in sources:
        index = sources.index(source)
        source_obj = Source(source)
        list_of_article_urls = source_obj.articles
        list_of_articles = []

        for url in list_of_article_urls:
            article = Article(url, source)
            list_of_articles.append(article)
            print(article.url)
            print(article.headline)
            print(article.summary)
            print("\n")

        upload_to_mongo(list_of_articles, collections[index])