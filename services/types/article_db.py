from .article_abstract import ArticleAbstract
from sqlalchemy import create_engine, Column, Integer, String, update
from sqlalchemy.orm import sessionmaker, declarative_base
from database.models.article import Article
class ArticleDB(ArticleAbstract):
    """ Function for working with articles in DataBase"""
    def __init__(self):
        #connect to db
        engine = create_engine("mysql+mysqlconnector://root:root@192.168.31.62:3312/test", echo=False)
        Session = sessionmaker(bind=engine)
        self.session = Session()
    def showAll(self):
        # # get articles data from database (in database format)
        db_articles = self.session.query(Article).all()
        return Article.many_to_dict(db_articles)

        # # create list that will contain dictionaries of article data
        # articles = []
        # # transfer db data to our `articles` list
        # for db_article in db_articles:
        #     # copy database data to dictionary so we will be able to display it in POSTMAN
        #     articles.append(db_article.to_dict())
        # # we have the code above inside Article.many_to_dict(articles)
        # return articles

    def showId(self, id):
        db_article = self.session.query(Article).filter(Article.id==id).first()
        if db_article:
            return db_article.to_dict()
        return None


    def addNew(self, params):
        print(params)
        new_article = Article(name=params['name'], description=params['description'], author=params['author'])
        self.session.add(new_article)
        self.session.commit()
        # we can use both ways to return all article
        return new_article.to_dict()
        # return self.showAll()



    def deleteId(self, id):
        # del_article = self.session.query(Article).filter(Article.id==id).first()
        # if del_article:
        #     self.session.delete(del_article)
        #     self.session.commit()
        #     return True
        # return False
        try:
            del_article = self.session.query(Article).filter(Article.id == id).delete()
            self.session.commit()
            return True
        except:
            return False

    def changeId(self, id, params):
        # 1#
        # db_article = self.session.query(Article).filter(Article.id == id).first()
        # db_article.name = params['name']
        # db_article.description = params['description']
        # db_article.author = params['author']
        # self.session.commit()

        # 2#
        # update_query = (
        #     update(Article).
        #     where(Article.id==id).
        #     values(name=params['name'], description=params['description'], author=params['author'])
        # )
        # self.session.execute(update_query)
        # self.session.commit()

        return False

