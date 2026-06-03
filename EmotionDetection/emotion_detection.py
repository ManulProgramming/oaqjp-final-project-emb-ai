import requests
import json
def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputs = {"raw_document": {"text":text_to_analyze}}
    response=requests.post(URL,headers=headers,json=inputs)
    final_response={
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }
    if response.status_code == 200:
        try:
            response_json=response.json()
            emotions=response_json.get('emotionPredictions',None)
            if emotions and len(emotions)==1:
                emotions=emotions[0].get('emotion',None)
                if emotions:
                    final_response={
                        "anger": emotions.get('anger',None),
                        "disgust": emotions.get('disgust',None),
                        "fear": emotions.get('fear',None),
                        "joy": emotions.get('joy',None),
                        "sadness": emotions.get('sadness',None),
                        "dominant_emotion": max(emotions,key=emotions.get)
                    }
        except (IndexError, KeyError, ValueError, TypeError) as e:
            None
    return final_response