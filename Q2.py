import numpy as np

def load_data(filename,T):

    data_array = [T(line.strip()) for line in open(filename, 'r')]

    return data_array

def get_Fano_factor(data_array,WIDTH,interval,big_t):
    width = int(WIDTH/interval)
    spike_count = []
    k=0
    for i in range(0,int(big_t/WIDTH)):
        m=0
        for j in range(k,k+width):
            if data_array[j] == 1:
                 m += 1
        spike_count.append(m)
        k += width
    average = np.mean(spike_count)
    variance = np.var(spike_count)
    Fano_factor=variance/average
    return Fano_factor

def get_coeffcient(data_array,interval):
    num=0
    intervals=[]
    for i in range(0,len(data_array)):
        if data_array[i] == 0:
            num += 1
        else:
            num += 1
            INTV = num*interval
            intervals.append(INTV)
            num = 0
    average=np.mean(intervals)
    std_deviation=np.std(intervals)
    coeffcient=std_deviation/average
    return(coeffcient)

sec=1.0
ms=0.001
interval=2*ms
big_t=1200*sec  #T

width = [10*ms,50*ms,100*ms]
spikes=load_data("rho.dat",int)

coeffcient = get_coeffcient(spikes,interval)
print('coefficient',coeffcient)
Fano_factor = get_Fano_factor(spikes,width[0],interval,big_t)
print('Fano_factor with 10ms ',Fano_factor)
Fano_factor2 = get_Fano_factor(spikes,width[1],interval,big_t)
print('Fano_factor with 50ms ',Fano_factor2)
Fano_factor3 = get_Fano_factor(spikes,width[2],interval,big_t)
print('Fano_factor with 100ms ',Fano_factor3)

