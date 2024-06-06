import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust microphone for ambient noise
        audio = recognizer.listen(source)  # Listen for audio input
        
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  # Use Google Web Speech API to recognize speech
        print("Recognized text:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

if __name__ == "__main__":
    recognize_speech()
