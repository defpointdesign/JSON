from .article_abstract import ArticleAbstract
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from database.sqlalchemy_create_table import Article
class ArticleDB(ArticleAbstract):
    """ Function for working with articles in DataBase"""
    def __init__(self):
        #connect to db
        engine = create_engine("mysql+mysqlconnector://root:root@192.168.31.62:3312/test", echo=False)
        Session = sessionmaker(bind=engine)
        self.session = Session()
    def showAll(self):
        # get articles data from database (in database format)
        db_articles = self.session.query(Article).all()

        # create list that will contain dictionaries of article data
        articles = []

        # transfer db data to our `articles` list
        for db_article in db_articles:
            # copy database data to dictionary so we will be able to display it in POSTMAN
            articles.append(db_article.to_dict())

        # we have the code above inside Article.many_to_dict(articles)

        return articles

    def showId(self, id):
        return {}

    def addNew(self, params):
        return {}


    def deleteId(self, id):
        return {}


    def changeId(self, id, params):
        return {}
