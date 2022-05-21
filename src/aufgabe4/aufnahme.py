import pyaudio
import numpy
import matplotlib.pyplot as plt
FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 100
p = pyaudio.PyAudio()
print('running')
stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,
input=True,frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES*FRAMESIZE)
decoded = numpy.fromstring(data, 'Int16');

stream.stop_stream()
stream.close()
p.terminate()
print('done')

count = 8000
start = 0
end = 0
for i in decoded[0:len(decoded)]:
    if i > 4000:
        start = count
        print("Start: " + str(start))
        break
    count += 1
    
trigger = decoded[start:start + SAMPLEFREQ]


numpy.save('sound', trigger)

plt.plot(decoded)
plt.plot(trigger)
plt.xlabel("Zeit in ms")
plt.ylabel("Amplitude")
plt.show()