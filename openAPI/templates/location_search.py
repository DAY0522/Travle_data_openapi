# _*_ coding: utf-8 _*_
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return 'welcome to flask'

@app.route('/location', methods=['POST'])
def handle_post():
    params = json.loads(request.get_data()) # str to json
    if len(params) == 0:
        return 'No parameter'

    print(params)
    return params['status']

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port='5000', debug=True)