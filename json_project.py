from flask import Flask, abort, request
import json

app = Flask(__name__)
FILE_NAME = 'dict.json'
@app.route('/articles')
def articles():
    data = ''
    with open(FILE_NAME, 'r') as file:
        data = json.load(file)
    return data

@app.route('/articles/<id>')
def ar_id(id):
    data = ''
    with open(FILE_NAME, 'r') as file:
        data = json.load(file)
        for article in data:
            if str(article['id']) == id:
                return article
        abort(404)

@app.route('/articles/create', methods=["POST"])
def ar_create():
    data = {}
    params=request.form.to_dict()
    with open(FILE_NAME, 'r') as json_file:
        data = json.load(json_file)
        params['id'] = data[-1]['id']+1
        data.append(params)

    with open(FILE_NAME, 'w') as json_file:
        json.dump(data, json_file)
    return data

@app.route('/articles/delete/<id>', methods=["DELETE"])
def ar_del(id):
    with open(FILE_NAME, 'r') as file:
        data=json.load(file)
        for index, article in enumerate(data):
            if str(article['id']) == id:
                del data[index]
    with open(FILE_NAME, 'w') as json_file:
        json.dump(data, json_file)
    return data

if __name__ == "__main__":
    app.run(debug=True)
