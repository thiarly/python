import pandas as pd
import matplotlib.pyplot as plt
x = pd.read_excel("/Users/thiarly/Documents/MEUSPROJETOS/python/diversos/b3/base.xlsx")

#plt.plot(x["idade"])
#plt.hist(x["idade"])
#plt.hist(x["idade"],bins=20)
plt.pie(x["idade"], labels= x["nome"],autopct="%1.2f%%")

plt.show()





