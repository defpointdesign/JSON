from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql+mysqlconnector://root:root@192.168.31.62:3312/test", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
class Article (Base):
    __tablename__='articles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))
    author = Column(String(50))

    #
    def to_dict(self):
        return { 'name': self.name, 'description': self.description, 'author': self.author, id: self.id }

    @staticmethod
    def many_to_dict(articles):
        data = []

        for article in articles:
            data.append(article.to_dict())

        return data

Base.metadata.create_all(engine)

article1 = Article(name="Building", description="Architectury", author="Yuliia")
article2 = Article(name="Pink", description="Woodworking", author="Oleksii")
article3 = Article(name="Without", description="Kindergarten", author="Illiia")

session.add_all([article1, article2, article3])
session.commit()




