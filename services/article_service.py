from services.types import ArticleAbstract, ArticleJson, ArticleDB

class ArticlesService:
    @staticmethod
    def getInstance() -> ArticleAbstract:
        # if(True):
        #     return ArticleJson()
        # else:
        return ArticleDB()








