from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return jsonify(result='to jest test')


@app.route('/test', methods=['POST'])
def test_post():
    request_data = request.get_json()

    # Tutaj można podać kod statusu np. 201(Created) return request_data, 201
    return request_data


app.run()
