from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positivo 😊"
    elif polarity < 0:
        sentiment = "Negativo 😠"
    else:
        sentiment = "Neutro 😐"

    return render_template('result.html', sentiment=sentiment, polarity=polarity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
