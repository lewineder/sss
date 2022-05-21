import numpy as np

import matplotlib.pyplot as plt

#Aufgabe1 c)
data = np.load("sound.npy")

fouriertransformierte = np.fft.fft(data)
aufnehmsekunden = 1

print("da: %s" % np.max(fouriertransformierte))

frequencys = []
for i in range(len(fouriertransformierte)):
    frequencys.append(i / aufnehmsekunden)


fig2, ax2 = plt.subplots()
ax2.plot(frequencys, np.abs(fouriertransformierte))
ax2.set_xlabel('Frequenz (Hz)')
ax2.set_ylabel('Amplitude')
ax2.set_title("Amplitudenspektrum")
plt.show()

