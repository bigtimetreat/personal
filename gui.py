from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Line
from sound_wave_animation import SoundWaveAnimation

class SoundWave(BoxLayout):
    def __init__(self, **kwargs):
        super(SoundWave, self).__init__(**kwargs)
        self.label = Label(text="Assistant Speaking...")
        self.add_widget(self.label)
        self.sound_wave_animation = SoundWaveAnimation()
        self.sound_wave_animation.start_animation()

    def update_wave(self, *args):
        self.canvas.clear()
        with self.canvas:
            Line(points=[100, 100, 200, 200, 300, 100], width=2)

class MyApp(App):
    def build(self):
        sound_wave = SoundWave()
        return sound_wave

if __name__ == "__main__":
    MyApp().run()
