import pyttsx3
import speech_recognition as sr

def recognize_speech():
    """
    Recognizes speech from the microphone.
    
    Returns:
        str: Transcribed text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust microphone for ambient noise
        audio_data = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcribed text:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def speak(text):
    """
    Converts text to speech and plays it.
    
    Args:
        text (str): The text to be spoken.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        try:
            # Listen for speech input
            text = recognize_speech()
            
            # Process the speech input and provide a response
            if text:
                # Example response
                response = "You said: " + text
                print("Response:", response)
                
                # Speak the response
                speak(response)
        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
