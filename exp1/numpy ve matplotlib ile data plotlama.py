
#%%
# plotting with numpy and matplotlib

import numpy as np
import matplotlib.pyplot as plt


t = np.arange(0., 5., 0.2) # evenly sampled times at 200ms intervals

plt.plot(t, t, 'r--', t, t**2,'bs',t,t**3,'g^') # red dashes, blue squares and green triangles
plt.show()


mu, sigma = 100,15
x = mu + sigma * np.random.randn(10000)

n,bins,patches = plt.hist(x, 50, density = 1, facecolor = 'g', alpha = 0.75) #histogram of data
plt.xlabel('A quantity')
plt.ylabel('Probability')
plt.title('Histogram of relationsip btw the quantity')
plt.text(60, .025, r'$\mu = 100,\ \sigma=15$') # 60, 0.025 koordinatlarına yazıyı yerleştirdi
plt.axis([20,180,0,0.03]) # axis aralıkları, ilk iki argüman x'in diğerleri y'nin
plt.grid(True)
plt.show()

