from numpy import *
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename,T):
    data_array = [T(line.strip()) for line in open(filename, 'r')]
    return data_array

def compute_sta(stim, rho, width,samprat,interval,flag):
    num_timesteps = int(width/samprat)
    sta_ = zeros(num_timesteps)
    spike_T = np.nonzero(rho)[0]           #non_zero spikes
    spike_times=[]
    if flag==1:   #spikes are not neccesarily adjacent
        m=0
        s = zeros(len(stim))
        while m < len(spike_T):
            s=spike_T[m]+interval
            if rho[int(s)]!=0:
                spike_times.append(spike_T[m])
            m+=1
    if flag==0:   #spikes are neccesarily adjacent
        m=0
        s = zeros(len(stim))
        while m < len(spike_T):
            s=spike_T[m]+interval
            if rho[int(s)]!=0:
                s1=rho[int(spike_T[m])+1:int(spike_T[m]+interval)]
                if sum(s1)== 0:
                    spike_times.append(spike_T[m])
            m+=1
    num = len(spike_times)
    for i in range(0, num_timesteps):
        x=0
        window=[]
        for j in range(0, num):
            if spike_times[j] - i < 0:
                x += 1
            window.append(stim[spike_times[j] - i])
        sta_[i] = sum(window) / (num - x)
    return sta_
ms=1
interval=[2*ms,10*ms,20*ms,50*ms,]
width = 100*ms

stimulus=load_data("stim.dat",float)
spikes=load_data("rho.dat",int)

sta1 = compute_sta(stimulus, spikes, width, 2,interval[0]/2,1)
sta2 = compute_sta(stimulus, spikes, width, 2,interval[1]/2,1)
sta3 = compute_sta(stimulus, spikes, width, 2,interval[2]/2,1)
sta4 = compute_sta(stimulus, spikes, width, 2,interval[3]/2,1)
time = [ i for i in range (2,101,2)]
print(sta4)

plt.plot(time, sta1,color='red',label='2ms')
plt.plot(time, sta2,color='green',label='2ms')
plt.plot(time, sta3,color='black',label='20ms')
plt.plot(time, sta4,color='yellow',label='50ms')
plt.legend()
plt.xlabel('Time (ms)')
plt.ylabel('Sta')
plt.title('spikes are not neccesarily adjacent')
plt.savefig('not neccesarily adjacent')
plt.show()

sta5 = compute_sta(stimulus, spikes, width, 2,interval[0]/2,0)
sta6 = compute_sta(stimulus, spikes, width, 2,interval[1]/2,0)
sta7 = compute_sta(stimulus, spikes, width, 2,interval[2]/2,0)
sta8 = compute_sta(stimulus, spikes, width, 2,interval[3]/2,0)
time = [ i for i in range (2,101,2)]

plt.plot(time, sta5,color='red',label='2ms')
plt.plot(time, sta6,color='green',label='2ms')
plt.plot(time, sta7,color='black',label='20ms')
plt.plot(time, sta8,color='yellow',label='50ms')

plt.legend()
plt.xlabel('Time (ms)')
plt.ylabel('Sta')
plt.title('spikes are adjacent')
plt.savefig('adjacent')
plt.show()
