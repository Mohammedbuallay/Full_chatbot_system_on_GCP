from google.cloud import texttospeech
import os, dialogflow
from playsound import playsound
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= 'modx-7c366-a60fb8dbc5ea.json'

client_stt = texttospeech.TextToSpeechClient()
voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

session_client = dialogflow.SessionsClient()
session = session_client.session_path('modx-7c366','1')

def text_to_speech(input_text):    
    synthesis_input = texttospeech.SynthesisInput(text=input_text)    
    response = client_stt.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

    playsound("output.mp3")


def send_to_dialogflow(text_to_be_analyzed):
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code='en')
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text

#text_to_speech('hello mohammed how are you')