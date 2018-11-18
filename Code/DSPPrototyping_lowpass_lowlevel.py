# Implementation of Butterworth second order filter by the following difference equation:
# y(n) = ao * x(n) + a1 * x(n - 1) + a2 * x(n-2) - b1 * y(n-1) - b2 * y(n-2)

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.io import wavfile

    fs, data = wavfile.read("331025__dshoot85__orchestral-loop-with-oriental-touch-mono.wav")
    data = data / 2.0 ** 15

    cutoff = 2000.0 #Cutoff Frequency in Hz

    # Calculate second-order Butterworth filter coefficients (Low pass)
    filterLambda = 1 / np.tan(np.pi * cutoff / fs)
    a0 = 1 / (1 + 2 * filterLambda + filterLambda ** 2)
    a1 = 2 * a0
    a2 = a0
    b1 = 2 * a0 * (1 - filterLambda ** 2)
    b2 = a0 * (1 - 2 * filterLambda + filterLambda ** 2)

    xn_1 = 0.0
    xn_2 = 0.0
    yn_1 = 0.0
    yn_2 = 0.0

    y = np.zeros(len(data))

    for n in range (0, len(data)):
        y[n] = a0 * data[n] + a1 * xn_1 + a2 * xn_2 - b1 * yn_1 - b2 * yn_2
        xn_2 = xn_1
        xn_1 = data[n]
        yn_2 = yn_1
        yn_1 = y[n]

    #Plot spectrogram
    plt.figure()
    plt.clf()
    plt.axes(xlabel="Time (seconds)", ylabel="Frequency (Hz)")
    plt.specgram(y, NFFT=512, Fs=fs, cmap=plt.cm.gist_gray)
    plt.plot()
    plt.show()

    wavfile.write("filtered_output.wav", fs, y)