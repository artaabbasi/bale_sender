from flask import Flask, request, jsonify
import requests
import json
app = Flask(__name__)


@app.route('/send/', methods=['POST'])
def test_gpt():
    payload = request.json
    api_token = payload.pop("api_token")
    r = requests.post(f'https://tapi.bale.ai/bot{api_token}/sendMessage', data=json.dumps(payload))
    return r.text