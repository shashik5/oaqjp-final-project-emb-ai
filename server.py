"""
Flask web server for the Emotion Detector application.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def render_index():
    """Render the main index page."""
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Handle emotion detection requests.

    Query Parameters:
        textToAnalyze (str): The text to analyze for emotions.

    Returns:
        str: A formatted string with emotion scores and dominant emotion,
             or an error message for blank input.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again.'

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
