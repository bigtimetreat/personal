import vosk
import sounddevice as sd
import json
import os

# Path to your Vosk model directory
model_dir = "/workspaces/personal/ai_personal_assistant/models/vosk-model-cn-0.22"
model = vosk.Model(model_dir)
rec = vosk.KaldiRecognizer(model, 16000)

def recognize_speech():
    def callback(indata, frames, time, status):
        if rec.AcceptWaveform(indata):
            result = rec.Result()
            result_dict = json.loads(result)
            print(result_dict['text'])
            return result_dict['text']
        else:
            partial_result = rec.PartialResult()
            partial_result_dict = json.loads(partial_result)
            print(partial_result_dict['partial'])
            return partial_result_dict['partial']
    
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
        print("Listening...")
        while True:
            pass
