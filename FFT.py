import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
import os
import pandas as pd

file_path = r"/2nd_test/"
file_list = os.listdir(file_path)

i = int(input("Enter the file you want to check:\t"))

rawdata = pd.read_csv(os.path.join(file_path, os.listdir(file_path)[i]),sep = '\t', header = None)

N = 20480
SR = 20480
T = 1/SR

xf = np.linspace(0.0,np.int(1//(2*T)),np.int(SR//2))

plt.figure(1)
plt.title(str(i)+"  B1 FFT") 
b1fft = fft(rawdata[0].values)
print("FFT of Bearing 1:\t",b1fft)
plt.plot(xf[1:], (2.0/N) * np.abs(b1fft[1:np.int(SR//2)]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Accel (g)')

plt.figure(2)
plt.title(str(i)+"  B2 FFT")  
b2fft = fft(rawdata[1].values)
print("FFT of Bearing 2:\t",b2fft)
plt.plot(xf[1:], (2.0/N) * np.abs(b2fft[1:np.int(SR/2)]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Accel (g)')


plt.figure(3)
plt.title(str(i)+"  B3 FFT")  
b3fft = fft(rawdata[2].values)
print("FFT of bearing 3:\t",b3fft)
plt.plot(xf[1:], (2.0/N) * np.abs(b3fft[1:np.int(SR/2)]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Accel (g)')


plt.figure(4)
plt.title(str(i)+"  B4 FFT")  
b4fft = fft(rawdata[3].values)
print("FFT of bearing 4", b4fft)
plt.plot(xf[1:], (2.0/N) * np.abs(b4fft[1:np.int(SR/2)]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Accel (g)')
