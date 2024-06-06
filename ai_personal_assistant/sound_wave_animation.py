import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from text_to_speech import speak

class SoundWaveAnimation:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.x = np.linspace(0, 2 * np.pi, 100)
        self.line, = self.ax.plot(self.x, np.sin(self.x))
        plt.show(block=False)

    def audio_callback(self, indata, frames, time, status):
        volume_norm = np.linalg.norm(indata) * 10
        self.line.set_ydata(np.sin(self.x + volume_norm))
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def start_animation(self):
        stream = sd.InputStream(callback=self.audio_callback)
        with stream:
            plt.show()

# Test the SoundWaveAnimation class
if __name__ == "__main__":
    animation = SoundWaveAnimation()
    animation.start_animation()
    speak("Welcome to the sound wave animation!")
