import azure.cognitiveservices.speech as speechsdk
import wave

def TTS(speech_key, service_region):
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # azure 여성음성 리스트
    # ko-KR-SunHiNeural, ko-KR-JiMinNeural, ko-KR-SeoHyeonNeural, ko-KR-SoonBokNeural, ko-KR-YuJinNeural
    speech_config.speech_synthesis_voice_name = "ko-KR-SoonBokNeural"

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    text = '옛날 옛적 아주 옛적 , 어느 나라 임금 한 분이 잘 생긴 따님을 여러 사람 데리고 계셨었는데'

    result = speech_synthesizer.speak_text_async(text).get()

    # Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        # 오디오 파일 저장
        audio_data = result.audio_data
        file_path = "./media/audio/output.mp3"
        with wave.open(file_path, 'wb') as wave_file:
            wave_file.setnchannels(1)
            wave_file.setsampwidth(2)
            wave_file.setframerate(16000)  # Adjust the sample rate if needed
            wave_file.writeframes(audio_data)

        print(f"Speech synthesized to {file_path}")
        return text
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")