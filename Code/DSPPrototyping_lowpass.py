from scipy.signal import butter, lfilter


def butter_lowpass(cutoff, fs, order):
    nyquist = 0.5 * fs
    cut = cutoff / nyquist
    b, a = butter(order, cut, btype='low')
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz
    from scipy.io import wavfile

    fs, data = wavfile.read("331025__dshoot85__orchestral-loop-with-oriental-touch-mono.wav")
    data = data / 2.0 ** 15

    cutoff = 2000.0 #Cutoff Frequency in Hz

    # Plot the frequency response for a few different orders.
    figureCounter = 1
    for order in [2, 4, 8]:
        b, a = butter_lowpass(cutoff, fs, order)
        w, h = freqz(b, a)
        plt.figure()
        plt.clf()
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Gain')
        plt.grid(True)
        plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)
        plt.legend(loc='best')

    #Filter the signal and plot spectrogram
    filtered = butter_lowpass_filter(data, cutoff, fs, 8)
    plt.figure()
    plt.clf()
    plt.axes(xlabel="Time (seconds)", ylabel="Frequency (Hz)")
    plt.specgram(filtered, NFFT=512, Fs=fs, cmap=plt.cm.gist_gray)
    plt.plot()
    plt.show()

    wavfile.write("filtered_output.wav", fs, filtered)