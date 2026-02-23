import matplotlib.pyplot as plt

sizes = [15, 30, 35, 20]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()