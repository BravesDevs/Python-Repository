import numpy as np
import matplotlib.pyplot as plt
print(2*np.pi)
# %matplotlib inline
x=np.linspace(0,2*np.pi,100)
y=np.sin(x)
print(x)
print(y)
plt.plot(x,y)
plt.show()