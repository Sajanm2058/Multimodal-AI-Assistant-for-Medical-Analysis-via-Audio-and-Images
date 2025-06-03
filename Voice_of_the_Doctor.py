# Step1: Setup Text to Speech-TTS- model with gTTS 
from gtts import gTTS

def text_to_speech_with_gTTS_old(input_text, output_filepath):
    language = 'en'

    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

#input_text = "Hi, this is Sajan with AI"
#text_to_speech_with_gTTS_old(input_text=input_text,output_filepath= 'gtts_testingpy.mp3')
   

# Step1b: Setup Text to Speech-TTS- model with  ElevenLabs
# import elevenlabs
# from elevenlabs.client import ElevenLabs


# import os
# ELEVENLABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY')

# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio = client.generate(
#         text=input_text,
#         voice="Aria",
#         output_format="mp3_22050_32",
#         model="eleven_turbo_v2",
#     )
#     elevenlabs.save_audio(audio, output_filepath)

# text_to_speech_with_elevenlabs(input_text,output_filepath= 'elevenlabs_testing.mp3')







# Step2: Use Model for Text output to Voice

import subprocess

import platform



from gtts import gTTS

def text_to_speech_with_gTTS(input_text, output_filepath):
    language = 'en'

    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()

    try:
        if os_name == 'Windows':
            subprocess.run(['powershell','-c',f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();' ])
        elif os_name == 'Darwin':  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name ==  'Linux' :
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError(f"Unsupported OS: {os_name}")
            
    except Exception as e:
        print(f"An error occurred while trying to play the audio file: {e}")

# input_text = "Hi, this is Sajan with AI autoplay"
#text_to_speech_with_gTTS(input_text=input_text,output_filepath= 'gtts_testingpy_autoplay.mp3')


