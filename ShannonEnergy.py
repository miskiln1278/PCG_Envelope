import array as arr
import wave
import struct
import numpy as np
import math
from matplotlib import pyplot as plt
import scipy.signal as scipy

#======================================================
#! Membuka File Wave

file = 'ragaJantung.wav'
f = wave.open(file)

frames = f.readframes(-1)
contoh = struct.unpack('h'*f.getnframes(), frames)
framerate = f.getframerate()
t = [float(i)/framerate for i in range(len(contoh))]
w = np.array(contoh)
s = w/32767

#=======================================================
#! Normalisasi
#b = np.list(contoh)
des = scipy.decimate(s,4, n=20, ftype='fir')

##filename = 'Data.txt'
##data = np.loadtxt(filename)
##np_data = np.array(data)
####fr = 8000
##amax = np.max(np_data)
##anorm = np_data / amax
##b = 20
#======================================================
#! Menghitung banyak data amplitudo pada file Wave
##N=0
##for i in np_data:
##    N+=1

#=======================================================
#! Shannon Energy

##hasil=np.concatenate((anorm[0:39], anorm))
##for i in range(40,len(anorm),20):
##        hasil=np.concatenate((hasil[0:i],anorm[b:-1]))
##        b=b+20
##        
##jmldata=math.floor(len(hasil) / 40)
##hasill=hasil[:(jmldata*40)]
##matrix40=(np.reshape(hasill,(40, jmldata), order="F")).T
##tmatrix = matrix40.conj().T
####print(np.shape(matrix40))
####print(np.shape(tmatrix))
##ES= -1*((matrix40** 2).dot(np.log10(tmatrix ** 2)))/40
##ESS=np.diag(ES)
##nESS=np.mean(ESS)
##stdESS=np.std(ESS)
##ESSa=(ESS - nESS) / stdESS
##haha=0
##for i in ESSa:
##    haha+=1
##fr = 2000
##tt = [float(i)/haha for i in range(len(ESSa))]
#========================================================
#! Ploting file wave

##from pylab import *
##plot(t, normis)
##plt.figure(figsize=(30, 4))
##plt.fill_between(255, ESSa)
###plt.xlim(jmldata[0], jmldata[-1]) 
##plt.xlabel('time (s)')
##plt.ylabel('freq (hz)')
##plt.savefig('hasilPlot.png', dpi=100)
##plt.figure(1)
##plt.subplot(211)
##plt.plot(anorm)
##plt.subplot(212)
##plt.plot(ESSa)
####plt.plot(tt,ESSa)
##plt.show()

#========================================================
#! Menyimpan data kedalam file *.txt
fff = open("Hasil_Des.txt", "w")
fff.write(str(des))
fff.close()




