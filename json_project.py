from flask import Flask, request
from services.article_service import ArticlesService

app = Flask(__name__)

@app.route('/articles')
def articles():
    articles = ArticlesService.getInstance().showAll()

    return articles

@app.route('/articles/<int:id>')
def articlesId(id):
    return ArticlesService.getInstance().showId(id)

@app.route('/articles/create', methods=["POST"])
def articlesCreate():
    params = request.form.to_dict()
    return ArticlesService.getInstance().addNew(params)

@app.route('/articles/delete/<id>', methods=["DELETE"])
def articlesDelete(id):
    return ArticlesService.getInstance().deleteId(id)

@app.route('/articles/modify/<id>', methods=["POST"])
def articlesModify(id):
    params = request.form.to_dict()
    return ArticlesService.getInstance().changeId(id, params)

if __name__ == "__main__":
    app.run(debug=True)
