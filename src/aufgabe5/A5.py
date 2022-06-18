import redlab as rl
import numpy as np
import time
import matplotlib.pyplot as plt

'''
print("------- einzelne Werte -------------------------")

print("16 Bit Value: " + str(rl.cbAIn(0,0,1)))
print("Voltage Value: " + str(rl.cbVIn(0,0,1)))

print("------- Messreihe -------------------------")

print("Messreihe: " + str(rl.cbAInScan(0,0,0,300,8000,1)))
print("Messreihe: " + str(rl.cbVInScan(0,0,0,300,8000,1)))


print("------- Ausgabe -------------------------")

print("Voltage Value: " + str(rl.cbVOut(0,0,101,2.5)))
'''

BoardNum = 0
Channel = 0
Rang = 101
DataValue = 5
    


def writeIn():
    rl.cbVOut(BoardNum, Channel, Rang, DataValue)
    
    
def writeOut():
    print(rl.cbVIn(BoardNum, Channel, 1))




#Aufgabe 2
#writeOut()
'''
Voltage1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
phillipsAnalog = (1.05, 2.1, 3.14, 4.07, 5.15, 6.05, 7.06, 8.1, 9.08, 9.9)
kathleyTRMS = (1.013, 2.065, 3.071, 3.982, 5.084, 5.994, 7.049, 8.056, 9.063, 9.974)
icoScpe = (1.008, 2.074, 3.081, 3.985, 5.073, 5.984, 7.028, 8.041, 9.063, 9.912)
redLabAD = (1.005859375, 2.060546875, 3.06640625, 3.974609375, 5.078125, 5.986328125, 7.05078125, 8.046875, 9.0625, 9.970703125)

#Aufgabe 3
#writeIn()

Voltage2 = (0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)
redLabDA = (0.510, 1.006, 1.514, 2.038, 2.533, 3.05, 3.558, 4.066, 4.567, 5.05)

#Aufgabe 4

sinus = [np.sin(2 * np.pi * (i/300)) for i in range(0,300)]

#a = sinus.add
print(sinus)

while(1):
    for i in range(0,300):
        rl.cbVOut(BoardNum, Channel, Rang, sinus[i] + 1)
        #time.sleep(1/300)

'''
#Aufgabe5
freq = 7400
sinus = rl.cbVInScan(0,0,0,1000,7000,1)
plt.plot(sinus)
#plt.plot(sinus[100:400])
#np.save(f'sinus_{freq}.png', sinus)



