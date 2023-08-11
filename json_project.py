from flask import Flask, request, abort
from services.article_service import ArticlesService

app = Flask(__name__)

@app.route('/articles')
def articles():
    articles = ArticlesService.getInstance().showAll()
    return articles

@app.route('/articles/<int:id>')
def articlesId(id):
    article=ArticlesService.getInstance().showId(id)
    if article:
        return article

    abort(404)

@app.route('/articles/create', methods=["POST"])
def articlesCreate():
    params = request.form.to_dict()
    ArticlesService.getInstance().addNew(params)

    return ArticlesService.getInstance().showAll()

@app.route('/articles/delete/<id>', methods=["DELETE"])
def articlesDelete(id):
    if ArticlesService.getInstance().deleteId(id):
        return ArticlesService.getInstance().showAll()

    abort(404)

@app.route('/articles/modify/<id>', methods=["POST"])
def articlesModify(id):
    params = request.form.to_dict()
    if ArticlesService.getInstance().changeId(id, params):
        return ArticlesService.getInstance().showAll()

    abort(404)


if __name__ == "__main__":
    app.run(debug=True)
