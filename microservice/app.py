from flask import Flask, jsonify, request
from microservice.generate import GenerateData

app = Flask(__name__)

client = app.test_client()

json = GenerateData().generate_json()
print(json)


@app.route('/', methods=['GET'])
def get_list():
    return jsonify(json)


@app.route('/', methods=['POST'])
def update_list():
    new_one = request.json
    json.append(new_one)
    return jsonify(json)


if __name__ == '__main__':
    app.run()
