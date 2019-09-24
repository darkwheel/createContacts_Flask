from flask import Flask, render_template, request, jsonify
from GoogleAccesser import GoogleAccesser

app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/square/', methods=['POST'])
def square():
    num = float(request.form.get('number', 0))
    squareNum = num ** 2
    data = {'square': squareNum}
    data = jsonify(data)
    return data


@app.route('/apikey1/', methods=['POST'])
def apikey1():
    apiKey = str(request.form.get('apinumber', 0))
    searchQuery = str(request.form.get('apinumber1', 0))
    print(apiKey)
    print(searchQuery)

    cardName = GoogleAccesser(apiKey, searchQuery)

    data = {'cardName': cardName}
    data = jsonify(data)
    return data


if __name__ == '__main__':
    app.run(debug=True)
