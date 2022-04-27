# periodic_sampling
A script to obtain periodic sampled data for non-periodic data given.

For using it you can do:

```
import httpimport
with httpimport.remote_repo(['periodic_sampling'], 'https://raw.githubusercontent.com/juanjq/periodic_sampling/main'):
     import periodic_sampling as sampling
```

An example can be done like this,

First we can generate the data randomly,

```
#generating random data
N = 20
y = np.random.rand(N)
x = np.sort(np.random.rand(N))*N
```

And we can plot it with ,

```
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(13,5))
ax1.plot(x,y,color='darkblue')
ax1.set_title('Original data')

ax2.plot(y,color='deeppink')
ax2.set_title('Periodic sampled data')
plt.show()
```

<p align="center">
    <img align="center" src="https://github.com/juanjq/periodic_sampling/blob/main/data/data.png?raw=true">
</p>

Where we can se de diference between randomly sampled data and uniformly sampled data. After that we re-sample the data with the script,

```
dt=0.5

sample_x,sample_y=sampling.resample(x,y,0.5)
```

And we can plot it with,
```
fig, ax = plt.subplots(figsize=(10,5))

ax.plot(x,y,'o-',color='b',label='Original')
ax.plot(sample_x,sample_y,'.--',color='r',label='Sampled',markersize=9)


ax.set_title('Re-sampled periodic data, dt = '+str(round(dt,2)))
plt.legend()
plt.show()
```

<p align="center">
    <img align="center" src="https://github.com/juanjq/periodic_sampling/blob/main/data/sampled.png?raw=true">
</p>

If we adjust the dt we can obtain as is expected better fitting results,

<p align="center">
    <img align="center" src="https://github.com/juanjq/periodic_sampling/blob/main/data/sampled2.png?raw=true">
</p>


