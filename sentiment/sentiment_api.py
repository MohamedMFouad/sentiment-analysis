from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

## Load the model or download if not present.
sentiment_analysis = pipeline("sentiment-analysis")

@app.route('/sentiment-analysis', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'Invalid request'}), 400

    result = sentiment_analysis(text)

    sentiment = result[0]['label']
    score = result[0]['score']

    return jsonify({'sentiment': sentiment, 'score': score}), 200

