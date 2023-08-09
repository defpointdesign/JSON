from services.article_service import ArticlesService

articles = ArticlesService.getInstance().showAll()
for article in articles:
    print(article.name)
