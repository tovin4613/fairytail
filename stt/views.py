from rest_framework.views import APIView
from rest_framework.response import Response
import azure.cognitiveservices.speech as speechsdk
import openai
import json

class RecognizeSpeechView(APIView):
    def post(self, request):
        with open ("key.json", "r") as f:
            key = json.load(f)
        speech_config = speechsdk.SpeechConfig(subscription=key["speech_key"], region=key["service_region"])
        speech_config.speech_recognition_language="ko-KR"

        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        result = {}
        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            result['text'] = speech_recognition_result.text
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            result['error'] = "No speech could be recognized: {}".format(speech_recognition_result.no_match_details)
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            result['error'] = "Speech Recognition canceled: {}".format(cancellation_details.reason)
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                result['error'] += " Error details: {}".format(cancellation_details.error_details)
        
        return Response(result)