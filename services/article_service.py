from services.json_service import JsonService

FILE_NAME = 'dict.json'
class ArticlesService:
    ''' Function for working with articles in JSON file'''
    @staticmethod
    def showAll():
        data = JsonService.readFile(FILE_NAME)
        return data

    @staticmethod
    def showId(id):
        data = JsonService.readFile(FILE_NAME)
        for article in data:
            if article['id'] == id:
                return article
            else: None

    @staticmethod
    def addNew(params):
        data = JsonService.readFile(FILE_NAME)
        params['id'] = data[-1]['id'] + 1
        data.append(params)
        JsonService.writeFile(FILE_NAME, data)
        return JsonService.readFile(FILE_NAME)

    @staticmethod
    def deleteId(id):
        data = JsonService.readFile(FILE_NAME)
        for index, article in enumerate(data):
            if str(article['id']) == id:
                del data[index]
        JsonService.writeFile(FILE_NAME, data)
        return JsonService.readFile(FILE_NAME)

    @staticmethod
    def changeId(id, params):
        data = JsonService.readFile(FILE_NAME)
        for article in data:
            if str(article['id']) == id:
                article['name'] = params['name']
                article['description'] = params['description']
                article['author'] = params['author']
                article['slug'] = params['slug']
        JsonService.writeFile(FILE_NAME, data)
        return data






