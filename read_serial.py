from serial import Serial
import sounddevice as sd
import numpy as np

volume = 0.5
fs = 44100
duration = 0.15
f = 440.0

sd.default.device = [7, 4]

ser = Serial('/dev/ttyACM0', 9600)
samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

while True:
    try:
        read = ser.readline()
        read = read.decode('utf-8')
        read = read.rstrip()
    except UnicodeDecodeError:
        continue
    try:
        read = int(read)
    except ValueError:
        continue

    if read == 1:
        sd.play(samples, fs)
        sd.wait()
        print('Movement!')
