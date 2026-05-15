import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

scores=np.random.normal(70,10,100)

plt.hist(scores,edgecolor="black")

plt.show()

