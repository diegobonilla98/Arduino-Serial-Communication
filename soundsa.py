import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

sd.default.device = [7, 4]  # input (>), output (<)

print(sd.query_devices())

volume = 1
fs = 44100
duration = 0.2
f = 440.0

samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)
sd.play(samples, fs)
print(sd.get_status())
sd.wait()

# print("Starting to record...")
# myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
# sd.wait()
#
# print("Playing back...")
# sd.play(myrecording, fs)
# sd.wait()

# plt.plot(myrecording)
# plt.show()
