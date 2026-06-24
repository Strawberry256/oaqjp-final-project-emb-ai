# Import the requests library to handle HTTP requests
import requests
import json

# Define a function named emotion_detector that takes a string input(text_to_analyse)
def emotion_detector(text_to_analyse):
    # URL of the emotion_detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # create a dictionary with the text to be analysed
    myobj = {"raw_document": {"text": text_to_analyse}}
    # set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    all_emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

    # Extracting the emotions and scores from the response
    required_emotions = ["anger", "disgust", "fear", "joy", "sadness"]
    filtered_emotions = {emotion: all_emotion_scores.get(emotion, 0) for emotion in required_emotions}

    dominant_emotion = max(filtered_emotions, key=filtered_emotions.get)

    # Returning a dictionary containing emotion detection results
    return {
        "dominant_emotion": dominant_emotion,
        "emotions": filtered_emotions
    }