import pyaudio
import speech_recognition as sr

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open microphone stream
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Initialize SpeechRecognition recognizer
recognizer = sr.Recognizer()

# Main loop to continuously listen for audio input
while True:
    try:
        # Read audio data from the microphone stream
        data = stream.read(1024)

        # Perform speech recognition on the audio data
        text = recognizer.recognize_sphinx(data)

        # Output the transcribed text
        print("Transcribed text:", text)
    except Exception as e:
        print("Error:", e)

# Close microphone stream
stream.stop_stream()
stream.close()
audio.terminate()
