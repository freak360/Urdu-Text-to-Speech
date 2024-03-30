import azure.cognitiveservices.speech as speechsdk
import streamlit as st
from dotenv import find_dotenv, load_dotenv
import sys
import os

load_dotenv(find_dotenv())
subscription_key = os.getenv("SUBSCRIPTION_KEY")
region = "eastus"

# Azure TTS integration
def text_to_speech_asad(subscription_key, region, text, file_name):
    # Set up the speech configuration with your subscription key and service region
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    speech_config.speech_synthesis_voice_name = "ur-PK-AsadNeural"
    
    # Specify the audio output file
    audio_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    
    # Set up the text-to-speech synthesizer with the audio output configuration to save to a file
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    # Synthesize the text
    result = speech_synthesizer.speak_text_async(text).get()
    
    # Check the result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized to the file {file_name} for text [{text}]")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))


def text_to_speech_uzma(subscription_key, region, text, file_name):
    # Set up the speech configuration with your subscription key and service region
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    speech_config.speech_synthesis_voice_name = "ur-PK-UzmaNeural"
    
    # Specify the audio output file
    audio_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    
    # Set up the text-to-speech synthesizer with the audio output configuration to save to a file
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    # Synthesize the text
    result = speech_synthesizer.speak_text_async(text).get()
    
    # Check the result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized to the file {file_name} for text [{text}]")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))


def text_to_speech_salman(subscription_key, region, text, file_name):
    # Set up the speech configuration with your subscription key and service region
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    speech_config.speech_synthesis_voice_name = "ur-IN-SalmanNeural"
    
    # Specify the audio output file
    audio_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    
    # Set up the text-to-speech synthesizer with the audio output configuration to save to a file
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    # Synthesize the text
    result = speech_synthesizer.speak_text_async(text).get()
    
    # Check the result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized to the file {file_name} for text [{text}]")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))

def text_to_speech_gul(subscription_key, region, text, file_name):
    # Set up the speech configuration with your subscription key and service region
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    speech_config.speech_synthesis_voice_name = "ur-IN-GulNeural"
    
    # Specify the audio output file
    audio_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    
    # Set up the text-to-speech synthesizer with the audio output configuration to save to a file
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    # Synthesize the text
    result = speech_synthesizer.speak_text_async(text).get()
    
    # Check the result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized to the file {file_name} for text [{text}]")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))



def get_audio(text, speaker):
    output_file = "speech.mp3"
    if speaker == "Asad":
        text_to_speech_asad(subscription_key, region, text, output_file)
    if speaker == "Uzma":
        text_to_speech_uzma(subscription_key, region, text, output_file)
    if speaker == "Salman":
        text_to_speech_salman(subscription_key, region, text, output_file)
    if speaker == "Gul":
        text_to_speech_gul(subscription_key, region, text, output_file)

    st.audio(output_file)

def save_audio_stream(stream, output_file):
    try:
        with open(output_file, "wb") as file:
            file.write(stream.read())
    except IOError as error:
        print(error)
        sys.exit(-1)


def main():
    st.set_page_config(page_title="Text to Speech", page_icon="✨")
    st.header("Ivac's Text to Speech App")
    text = st.text_area("Input Urdu Text Here")
    speaker = st.radio("Select Voice", ["Asad", "Uzma", "Salman", "Gul"])
    if st.button("Generate"):
        get_audio(text, speaker)

if __name__ == "__main__":
    main()
