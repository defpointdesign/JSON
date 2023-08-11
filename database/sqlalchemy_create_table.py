from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from database.models.article import Article
from sqlalchemy.orm import declarative_base
Base = declarative_base()

engine = create_engine("mysql+mysqlconnector://root:root@192.168.31.62:3312/test", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

article1 = Article(name="Building", description="Architectury", author="Yuliia")
article2 = Article(name="Pink", description="Woodworking", author="Oleksii")
article3 = Article(name="Without", description="Kindergarten", author="Illiia")

session.add_all([article1, article2, article3])
session.commit()




