"""Module providing a server."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detection():
    """Emotion detection"""
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['anger'] is None:
        return "Invalid text! Please try again!."

    return f'For the given statement, the system response is "anger" : {response["anger"]}, \
    "disgust" : {response["disgust"]},"fear" : {response["fear"]},"joy" : {response["joy"]} \
     and "sadness" : {response["sadness"]}. The dominant emotion is \
     {response["dominant_emotion"]}.'

@app.route("/")
def render_index_page():
    """Renders the page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
