from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def get_emotion_detector():
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
            output += "'{}': {} and ".format(labels[i], scores[i])
        elif i == 4:
            output += "'{}': {}. ".format(labels[i], scores[i])
        else:
            output += "'{}': {}, ".format(labels[i], scores[i])

    output += "The dominant emotion is {}.".format(response["dominant_emotion"])
    return output


  
@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000)