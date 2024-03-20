from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/sentiment-analysis', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'Invalid request'}), 400

    start_time = datetime.now()

    result = requests.post("http://sentiment_service:3040/sentiment-analysis",
                           json={"text": text}).json()

    end_time = datetime.now()
    response_time = (end_time - start_time).total_seconds() * 1000  # in milliseconds

    sentiment = result['sentiment']
    score = result['score']

    return jsonify({'sentiment': sentiment, 'score': score, 'response_time': response_time}), 200