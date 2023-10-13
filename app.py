from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

@app.after_request
def remove_referrer_policy(response):
    del response.headers['Referrer-Policy']
    return response

@app.route('/send/', methods=['POST'])
def test_gpt():
    payload = request.json
    api_token = payload.pop("api_token")
    r = requests.post(f'https://tapi.bale.ai/bot{api_token}/sendMessage', data=json.dumps(payload))
    return r.text