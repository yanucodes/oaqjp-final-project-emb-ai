"""Run emotion detection using Watson NLP Library API."""
import json
import requests



URL = ("https://sn-watson-emotion.labs.skills.network/"
       "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
EMOTIONS = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']


def run_emotion_detector(text_to_analyze: str) -> dict:
    """
    Run emotion detection using Watson NLP Library API.

    Args:
        text_to_analyze: input text string

    Returns:
        A dictionary containing response from Watson NLP Library
    """
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=input_json, headers=HEADERS, timeout=60)
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        return response_dict
    else:
        return {'emotionPredictions': None, 'status_code': response.status_code}


def find_dominant_emotion(emotions: dict) -> str:
    """
    Find the dominant emotion in the text.

    Args:
        emotions: dictionary with emotions as keys and their scores as values.

    Returns:
        The name of the dominant emotion.
    """
    return max(emotions, key=emotions.get)


def emotion_detector(text_to_analyze: str) -> dict:
    """
    Detect emotions in text and return a dictionary with emotions scores and
    a dominant emotion.

    Args:
        text_to_analyze: input text string

    Returns:
        A dictionary containing scores for each emotion and the name of
        the dominant emotion
    """
    response = run_emotion_detector(text_to_analyze)
    if response['emotionPredictions'] is not None:
        emotions = response['emotionPredictions'][0]['emotion']
        emotions['dominant_emotion'] = find_dominant_emotion(emotions)
    else:
        emotions = {emotion: None for emotion in EMOTIONS}
    return emotions