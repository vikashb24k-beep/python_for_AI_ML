import matplotlib.pyplot as plt
import numpy as np
# data=[7,8,5,6,9,4,10,12,15]

# plt.boxplot(data)
# plt.grid()

# plt.show() 

group1=np.random.normal(50,10,100)
group2=np.random.normal(60,15,100)


# plt.boxplot(group1,label="group1")
# plt.boxplot(group2,label="group2")
# plt.legend()


plt.boxplot([group1,group2],tick_labels=["group1","group2"])

plt.show()