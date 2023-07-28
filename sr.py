import speech_recognition as sr
from pocketsphinx import LiveSpeech


class Ears:

    OPENAI_API_KEY = "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"
    r = sr.Recognizer()

    lang = 'en'

    def __init__(self):
        self.lang = 'en'

    @classmethod
    def listen(cls):
        print('speak')
        speech = speech = LiveSpeech(lm=False, kws='C:/Users/fhernandez/Desktop/Projects/Python/AI/keys.list', dic='C:/Users/fhernandez/Desktop/Projects/Python/AI/keys.dict')
        for phrase in speech:
                with sr.Microphone() as source:
                    Ears.r.adjust_for_ambient_noise(source, duration=3)
                    print(">>>")
                    audio = Ears.r.listen(source)
                print('<<<')
                return Ears.process(audio)

    @classmethod
    def process(cls, audio):
        try:
            return Ears.r.recognize_whisper_api(audio, api_key=Ears.OPENAI_API_KEY)
        except sr.RequestError as e:
            return "Come again."


