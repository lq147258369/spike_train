import random as rnd
import numpy as np

def get_spike_train(rate,big_t,tau_ref):
    if 1 <= rate*tau_ref:
        print("firing rate not possible given refractory period f/p")
        return []
    exp_rate = rate/(1-tau_ref*rate)
    spike_train = []
    t=rnd.expovariate(exp_rate)   # 随机生成符合指数分布的随机数；exp_rate返回正,值[0, +∞]; exp_rate返回负,值[-∞, 0];返回值越小,获得值越大
    while t< big_t:
        spike_train.append(t) #方法向列表的尾部添加一个新的元素，只接受一个参数
        t += tau_ref+rnd.expovariate(exp_rate)
    return spike_train

def get_Fano_factor(spike_train,width,big_t):
    spike_count = np.zeros(int(big_t/width))
    for i in range(len(spike_train)):
        j = int(spike_train[i]/width)
        spike_count[j] += 1
    average = np.mean(spike_count)
    variance = np.var(spike_count)
    Fano_factor = variance/average
    return Fano_factor

def get_coeffcient(spike_train):
    interval = []
    for i in range(len(spike_train)-1):
        difference = spike_train[i+1]-spike_train[i]
        interval.append(difference)
    average = np.mean(interval)
    std_deviation = np.std(interval)
    coeffcient = std_deviation/average
    return(coeffcient)

Hz=1.0
sec=1.0
ms=0.001
rate=35.0 *Hz  #firing rate
tau_ref1=5*ms #refractory period
tau_ref2=0*ms
big_t=1000*sec  #T
width = [10*ms,50*ms,100*ms]

print('no refractory period')
spike_train=get_spike_train(rate,big_t,tau_ref2)
print('spike_train ',spike_train)
coeffcient = get_coeffcient(spike_train)
print('coefficient',coeffcient)
Fano_factor1 = get_Fano_factor(spike_train,width[0],big_t)
print('Fano_factor with 10ms is',Fano_factor1)
Fano_factor2 = get_Fano_factor(spike_train,width[1],big_t)
print('Fano_factor with 50ms is',Fano_factor2)
Fano_factor3 = get_Fano_factor(spike_train,width[2],big_t)
print('Fano_factor with 100msis',Fano_factor3)

print('refractory period of 5ms')
spike_train=get_spike_train(rate,big_t,tau_ref1)
print('spike_train ',spike_train)
coeffcient = get_coeffcient(spike_train)
print('coefficient',coeffcient)
Fano_factor1 = get_Fano_factor(spike_train,width[0],big_t)
print('Fano_factor with 10ms is',Fano_factor1)
Fano_factor2 = get_Fano_factor(spike_train,width[1],big_t)
print('Fano_factor with 50ms is',Fano_factor2)
Fano_factor3 = get_Fano_factor(spike_train,width[2],big_t)
print('Fano_factor with 100msis',Fano_factor3)
