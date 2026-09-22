"""Server for Emotion Detection Flask application"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def get_emotion_detector():
    """
    Get result of emotion detection with Watson NLP Library.

    Returns:
        Formatted text with the result of emotion detection in the text provided in request.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    # Extract the labels and scores from the response
    emotion_scores = {key: value for key, value in response.items() if key != "dominant_emotion"}
    labels = list(emotion_scores.keys())
    scores = list(emotion_scores.values())
    output = "For the given statement, the system response is "
    for i in range(5):
        if i == 3:
            output += f"'{labels[i]}': {scores[i]} and "
        elif i == 4:
            output += f"'{labels[i]}': {scores[i]}. "
        else:
            output += f"'{labels[i]}': {scores[i]}, "

    output += f"The dominant emotion is {response['dominant_emotion']}."
    return output


@app.route("/")
def render_index_page():
    """
    Render the main page for the web application.

    Returns:
        Rendered template for the main page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
