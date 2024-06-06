import os

def speak(text):
    os.system(f'espeak "{text}"')
