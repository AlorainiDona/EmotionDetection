# emotion_detection.py

import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        # If the input text is blank, return a dictionary with None values for all keys
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()  # Raise an error for bad responses

        # Check the status code for 400 and handle accordingly
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        # Extract the relevant information based on the actual structure of the response
        emotion_result = response.json().get('emotionPredictions', [])[0].get('emotion', {})

        # Format the output as required
        formatted_output = {
            'anger': emotion_result.get('anger', 0),
            'disgust': emotion_result.get('disgust', 0),
            'fear': emotion_result.get('fear', 0),
            'joy': emotion_result.get('joy', 0),
            'sadness': emotion_result.get('sadness', 0),
            'dominant_emotion': max(emotion_result, key=emotion_result.get)
        }

        return formatted_output

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
