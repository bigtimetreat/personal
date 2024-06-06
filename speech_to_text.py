import vosk
import sounddevice as sd

model = vosk.Model("model")
rec = vosk.KaldiRecognizer(model, 16000)

def recognize_speech():
    def callback(indata, frames, time, status):
        if rec.AcceptWaveform(indata):
            result = rec.Result()
            print(result)
            return result
        else:
            partial_result = rec.PartialResult()
            print(partial_result)
            return partial_result
    
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
        print("Listening...")
        while True:
            pass
