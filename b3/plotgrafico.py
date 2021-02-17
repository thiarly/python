import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1, 6) # 1, 2, 3, 4, 5, 6 
dados = np.random.randint(20, 30, 5)

plt.style.use('ggplot')
plt.ion()

plt.bar(x, dados)
plt.pause(5)
plt.bar(x, dados)


plt.ioff()


