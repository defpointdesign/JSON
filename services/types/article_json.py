from ..json_service import JsonService
from .article_abstract import ArticleAbstract

FILE_NAME = 'dict.json'
class ArticleJson(ArticleAbstract):
    """ Function for working with articles in JSON file"""
    def showAll(self):
        data = JsonService.readFile(FILE_NAME)
        return data

    def showId(self, id):
        data = JsonService.readFile(FILE_NAME)
        for article in data:
            if article['id'] == id:
                return article
            else:
                None

    def addNew(self, params):
        data = JsonService.readFile(FILE_NAME)
        params['id'] = data[-1]['id'] + 1
        data.append(params)
        JsonService.writeFile(FILE_NAME, data)
        return JsonService.readFile(FILE_NAME)

    def deleteId(self, id):
        data = JsonService.readFile(FILE_NAME)
        for index, article in enumerate(data):
            if str(article['id']) == id:
                del data[index]
        JsonService.writeFile(FILE_NAME, data)
        return JsonService.readFile(FILE_NAME)

    def changeId(self, id, params):
        data = JsonService.readFile(FILE_NAME)
        for article in data:
            if str(article['id']) == id:
                article['name'] = params['name']
                article['description'] = params['description']
                article['author'] = params['author']
                article['slug'] = params['slug']
        JsonService.writeFile(FILE_NAME, data)
        return data