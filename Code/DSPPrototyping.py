from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

fs, data = wavfile.read("331025__dshoot85__orchestral-loop-with-oriental-touch-mono.wav")
#fs, data = wavfile.read("sine_440Hz_44100fs_1sec.wav")

# It's a 16-bit mono file: normalize to range [-1,1]
data = data / 2.0 ** 15

plt.figure()
plt.clf()
plt.axes(xlabel="Time (seconds)", ylabel="Amplitude")
t = np.linspace(0, len(data) / float(fs), len(data))
plt.plot(t, data)

plt.figure()
plt.clf()
plt.axes(xlabel="Time (seconds)", ylabel="Frequency (Hz)")
plt.specgram(data, NFFT=512, Fs=fs, cmap=plt.cm.gist_heat)
plt.plot()

plt.figure()
plt.clf()
plt.magnitude_spectrum(data, Fs=fs, scale='dB')

plt.show()
