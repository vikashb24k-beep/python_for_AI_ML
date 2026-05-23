import matplotlib.pyplot as plt

people = ["Person A", "Person B", "Person C", "Person D", "Person E",
          "Person F", "Person G", "Person H", "Person I", "Person J"]

age = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]

blood_pressure = [110, 115, 120, 122, 125, 130, 135, 123, 145, 150]


plt.xlabel("age")
plt.ylabel("bp")


plt.scatter(age, blood_pressure)
plt.show()
