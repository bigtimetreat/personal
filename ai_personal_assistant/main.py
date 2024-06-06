from gui import MyApp
import time
from speech_to_text import recognize_speech

def main():
    # Start the GUI
    app = MyApp()
    app.run()

    # Continuously listen for audio input and transcribe it to text
    while True:
        try:
            text = recognize_speech()
            print("Transcribed text:", text)
            # You can add your logic here to handle the transcribed text
        except Exception as e:
            print("Error:", e)

        # Add a delay to reduce CPU usage
        # You can adjust the delay time as needed
        time.sleep(1)

if __name__ == "__main__":
    main()
