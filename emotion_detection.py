"""Run emotion detection using Watson NLP Library API."""
import requests


URL = ("https://sn-watson-emotion.labs.skills.network/"
       "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }


def emotion_detector(text_to_analyze: str) -> str:
    """
    Run emotion detection using Watson NLP Library API.

    Args:
        text_to_analyze: input text string

    Returns:
        A text string containing response from Watson NLP Library
    """
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=input_json, headers=HEADERS, timeout=60)
    return response.text
