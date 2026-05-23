import matplotlib.pyplot as plt

expense=['salary','rent','marketing','R&D']
amount=[500,150,200,75]

explod=[0,0,0,0.23]
plt.pie(amount,labels=expense,autopct='%1.1f%%',explode=explod,startangle=90,shadow=True)

plt.show()