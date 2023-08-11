from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
class Article (Base):
    __tablename__='articles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))
    author = Column(String(50))

    def to_dict(self):
        return { 'name': self.name, 'description': self.description, 'author': self.author, 'id': self.id }

    @staticmethod
    def many_to_dict(articles):
        data = []
        for article in articles:
            data.append(article.to_dict())

        return data


