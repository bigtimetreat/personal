from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from threading import Thread
from sound_wave_animation import SoundWaveAnimation
from text_to_speech import speak

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.label = Label(text="Transcribed text will appear here")
        self.toggle_button = ToggleButton(text="Hold to Talk", state="normal")
        self.toggle_button.bind(on_press=self.start_listening)
        self.toggle_button.bind(on_release=self.stop_listening)
        layout.add_widget(self.label)
        layout.add_widget(self.toggle_button)
        
        # Start sound wave animation in a separate thread
        sound_animation_thread = Thread(target=self.start_sound_wave_animation)
        sound_animation_thread.daemon = True  # Allow the thread to terminate with the main program
        sound_animation_thread.start()
        
        return layout

    def start_listening(self, instance):
        print("Start listening...")
        self.label.text = "Start talking..."
        self.transcription = ""
        # Code to start listening to the microphone

    def stop_listening(self, instance):
        print("Stop listening...")
        # Code to stop listening to the microphone
        self.label.text = "Transcribed text: " + self.transcription

    def start_sound_wave_animation(self):
        sound_animation = SoundWaveAnimation()
        sound_animation.start_animation()
        speak("Welcome to the sound wave animation!")

if __name__ == "__main__":
    MyApp().run()
