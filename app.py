from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/')
def searchsub():
    query_receive = request.args['subject']
    list(db.nonsul.find({'subject': {'$regex': query_receive}}))


@app.route('/nonsul')
def screening():
    screenings = list(db.nonsul.find({}, {'_id': 0}))
    result = {'result': 'success', "screenings" : screenings}
    return jsonify(result)

@app.route('/nonsul')
def areasel():
    areasels = list(db.nonsul.find({}, {'_id': 0}))
    result = {'result': 'success', "areasels" : areasels}
    return jsonify(result)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

