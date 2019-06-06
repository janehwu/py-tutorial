import numpy as np
import matplotlib.pyplot as plt

bp = np.genfromtxt("oil-data/BP.L.CSV", delimiter=',')
print(bp.shape)

close_prices = bp[:,3]
print(close_prices.shape)
x_vals = np.arange(close_prices.shape[0])

plt.plot(x_vals, close_prices)
plt.title("BP")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.show()
