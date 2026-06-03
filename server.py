"""
Start Flask web app, with EmotionDetector API.
Host on localhost:5000
"""

import re
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask('')

@app.route("/emotionDetector",methods=["GET"])
def emotion_detection():
    """
    Access EmotionDetector API.
    Returns a string formated JSON of the results.
    """
    text_to_analyze=request.args.get('textToAnalyze',None)
    if text_to_analyze:
        response=emotion_detector(text_to_analyze)
        dominant_emotion=response.get('dominant_emotion',None)
        if dominant_emotion:
            response_without_dom=response.copy()
            response_without_dom.pop('dominant_emotion',None)
            return "For the given statement, the system response is " + \
                re.sub(r'[{}]','',str(response_without_dom)) + \
                f". The dominant emotion is {dominant_emotion}."
    return 'Invalid text! Please try again!'

@app.route("/",methods=["GET"])
def index():
    """
    Render main home page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost",port=5000)
