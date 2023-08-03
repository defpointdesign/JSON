from JsonService import JsonService
from flask import abort, request

FILE_NAME = 'dict.json'
class ArticlesService:
    ''' Function for working with articles in JSON file'''
    def showAll(name):
        data = JsonService.readFile(FILE_NAME)
        return data

    def showId(name, id):
        data = JsonService.readFile(FILE_NAME)
        for article in data:
            if article['id'] == id:
                return article
        abort(404)

    def addNew(name):
        params = request.form.to_dict()
        data = JsonService.readFile(FILE_NAME)
        params['id'] = data[-1]['id'] + 1
        data.append(params)
        JsonService.writeFile(FILE_NAME, data)
        return JsonService.readFile(FILE_NAME)

    def deleteId(name, id):
        data = JsonService.readFile(FILE_NAME)
        for index, article in enumerate(data):
            if str(article['id']) == id:
                del data[index]
        JsonService.writeFile(FILE_NAME, data)
        return JsonService.readFile(FILE_NAME)

    def changeId(name, id):
        params = request.form.to_dict()
        data = JsonService.readFile(FILE_NAME)
        for article in data:
            if str(article['id']) == id:
                article['name'] = params['name']
                article['description'] = params['description']
                article['author'] = params['author']
                article['slug'] = params['slug']
        JsonService.writeFile(FILE_NAME, data)
        return JsonService.readFile(FILE_NAME)






