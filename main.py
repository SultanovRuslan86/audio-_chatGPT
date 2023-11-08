import speech_recognition as sr
import openai


import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

openai.api_key = api_key

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language='ru-RU')
        return text


def gpt_chat(input_text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,
        max_tokens=500
    )
    return response.choices[0].text.strip()

audio_file_path = 'example3.wav'
transcribed_text = transcribe_audio(audio_file_path)
response_from_gpt = gpt_chat(transcribed_text)

print('Распознанный текст:', transcribed_text)
print('Ответ от GPT:', response_from_gpt)


