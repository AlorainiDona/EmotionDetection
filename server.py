from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
def emotion_detector_route():
    """
    Route for emotion detection.

    Returns:
        JSON: Result of emotion detection.
    """
    if request.method == 'POST':
        data = request.get_json()
        text_to_analyze = data.get('text', '')
        result = emotion_detector(text_to_analyze)

        # Check if dominant_emotion is None and handle the error
        dominant_emotion = result.get('dominant_emotion')
        if dominant_emotion is None:
            return jsonify({"error": "Invalid text! Please try again."}), 400

        return jsonify(result)
def index():
    """
    Route for the index page.

    Returns:
        HTML: Rendered index page.
    """
    return render_template('index.html')
@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    return emotion_detector_route()
@app.route('/')
def index_route():
    return index()
if __name__ == '__main__':
    app.run(debug=True, port=5000)
