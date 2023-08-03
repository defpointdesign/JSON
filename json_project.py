from flask import Flask, abort, request
from ArticlesService import ArticlesService

app = Flask(__name__)

@app.route('/articles')
def aticles():
    return ArticlesService.showAll('FILE_NAME')

@app.route('/articles/<int:id>')
def articlesId(id):
    return ArticlesService.showId('FILE_NAME', id)

@app.route('/articles/create', methods=["POST"])
def articlesCreate():
    return ArticlesService.addNew('FILE_NAME')

@app.route('/articles/delete/<id>', methods=["DELETE"])
def articlesDelete(id):
    return ArticlesService.deleteId('FILE_NAME', id)

@app.route('/articles/modify/<id>', methods=["POST"])
def articlesModify(id):
    return ArticlesService.changeId('FILE_NAME', id)




# @app.route('/articles/create', methods=["POST"])
# def ar_create():
#     params=request.form.to_dict()
#     with open(FILE_NAME, 'r') as json_file:
#         data = json.load(json_file)
#         params['id'] = data[-1]['id']+1
#         data.append(params)
#     with open(FILE_NAME, 'w') as json_file:
#         json.dump(data, json_file)
#     return data

#
# @app.route('/articles/delete/<int:id>', methods=["DELETE"])
# def ar_del(id):
#     data = JsonService.readFile('FILE_NAME')
#     for index, article in enumerate(data):
#         if article['id'] == id:
#             del data[index]
#     JsonService.writeFile('FILE_NAME', data)
#     return data
#


# @app.route('/articles/modify/<id>', methods=["POST"])
# def mod_del(id):
#     params=request.form.to_dict()
#     with open(FILE_NAME, 'r') as file:
#         data=json.load(file)
#         for article in data:
#             if str(article['id']) == id:
#                 article['name'] =params['name']
#                 article['description'] = params['description']
#                 article['author'] = params['author']
#                 article['slug'] = params['slug']
#     with open(FILE_NAME, 'w') as json_file:
#         json.dump(data, json_file)
#     return data

if __name__ == "__main__":
    app.run(debug=True)
