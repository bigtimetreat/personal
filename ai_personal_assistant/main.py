from speech_to_text import recognize_speech
from text_to_speech import speak
from dialog_management import get_response
from vision_agent import capture_screen
from sound_wave_animation import SoundWaveAnimation
from gui import MyApp

def main():
    # Start the GUI
    app = MyApp()
    app.run()

if __name__ == "__main__":
    main()
