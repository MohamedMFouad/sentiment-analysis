from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/sentiment-analysis', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'Invalid request'}), 400

    result = requests.post("http://sentiment_service:3040/sentiment-analysis",
                         json = {"text": text}).json()
    # print(result, flush=True)
    sentiment = result['sentiment']
    score = result['score']

    return jsonify({'sentiment': sentiment, 'score': score}), 200


