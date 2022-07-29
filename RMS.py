# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

def RMS(lst,n):
    square = 0
    mean = 0.0
    root = 0.0
    for i in lst:
        square = square + pow(i, 2);
    mean = square/n;
    root = pow(mean,0.5);
    return root;

filepath = r"\2nd_test"

listfiles = os.listdir(filepath)
rmsplt = []

for i in listfiles:
    print(i)
    x = pd.read_csv(os.path.join(filepath,i), delimiter = '\t', header=None)
    N = 20480#length of the array
    Fs = 1 	#sample rat
    rms_val = RMS(x[0].values,N)
    print(rms_val)
    rmsplt.append(rms_val)
    plt.figure(1)
    plt.title("NASA IMS Bearing 1")
    plt.plot(rmsplt)
    plt.xlabel('Time (seconds)')
    plt.ylabel('RMS Accel (g)')
plt.plot([0.04]*1000,'g--',label = 'safe')
plt.plot([0.16]*1000,'y--', label = 'risky')
plt.plot([0.3]*1000,'r--',label = 'failed')
plt.legend()
plt.show()

